import os
from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from ..models import Projects, InstrumentsMeta, ExportFile
from ..tasks import generate_exports

upload_folder = settings.MEDIA_ROOT

exclude_fields = ['id', 'record_id', 'complete']


@login_required(login_url='/')
def render_export_reports_page(request, project_names):
    data = [{'tab_item': 'projects',
             'table_columns': get_project_columns(),
             'table_id': 'projectsList',
             'data_url': 'tsepamo:projects-details',
             'url_kwargs': {'project_names': project_names}},
            {'tab_item': 'instruments',
             'table_columns': get_forms_columns(),
             'table_id': 'instrumentsList',
             'data_url': 'tsepamo:instruments-details',
             'url_kwargs': {'project_names': project_names}},
            {'tab_item': 'fields',
             'table_columns': get_fields_columns(),
             'table_id': 'fieldsList',
             'data_url': '', }]

    return render(request, 'tsepamo/exports.html', {
        'selected_projects': project_names,
        'data': data,
    })


@login_required(login_url='/')
def render_projects_page(request):
    table_columns = get_project_columns()
    return render(
        request, 'tsepamo/projects.html', {'table_columns': table_columns})


@login_required(login_url='/')
def render_repository_page(request):
    latest_file = get_latest_export_file()
    repository_columns = get_repository_columns()
    return render(request, 'tsepamo/repository.html',
                  {'recent_file': latest_file,
                   'data_url': 'tsepamo:repository-details',
                   'table_columns': repository_columns})


@login_required(login_url='/')
def render_dashboard_page(request):
    project_details = get_project_details()
    return render(request, 'tsepamo/dashboard.html', {
        'project_details': project_details})


@login_required(login_url='/')
def project_data_view(request, project_names=''):
    if request.method == 'GET':
        project_names = project_names.split(',') if project_names else []
        project_details = get_project_details(project_names)
        return JsonResponse(project_details, safe=False)


@login_required(login_url='/')
def form_data_view(request, project_names):
    if request.method == 'GET':
        project_names = project_names.split(',')
        form_details = get_forms_details(project_names)
        return JsonResponse(form_details, safe=False)


@login_required(login_url='/')
def fetch_fields_view(request, instrument_names):
    if request.method == 'GET' and instrument_names:
        instrument_names = instrument_names.split(',')
        fields_data = []
        for name in instrument_names:
            fields_data.extend(get_fields_by_name(name))
        return JsonResponse(fields_data, safe=False)


@login_required(login_url='/')
def repository_data_view(request):
    if request.method == 'GET':
        repository_data = get_repository_details()
        return JsonResponse(repository_data, safe=False)


@login_required(login_url='/')
def project_fields(request, project_name):
    model_cls = django_apps.get_model('tsepamo', project_name)
    fields_tuple = model_cls._meta.fields
    fields = [{'name': field.name, 'verbose_name': field.verbose_name} for field in fields_tuple]
    return JsonResponse(fields, safe=False)


@csrf_exempt
@login_required(login_url='/')
def export_view(request):
    if request.method == 'POST':
        export_name = request.POST.get('export_name')
        export_type = request.POST.get('export_type')
        selected_fields = request.POST.get('selected_fields').split(',')
        selected_instruments = request.POST.get('selected_instruments').split(',')
        user_created = request.user.username
        user_email = request.user.email

        generate_exports.delay(export_name, user_created, [user_email, ], 'tsepamo',
                               export_type, selected_instruments, selected_fields)
        # export_cls = GenerateDataExports(
        #     export_name, user_created, 'tsepamo', export_types,
        #     selected_instruments, selected_fields,)
        return JsonResponse(
            {'status': 'CSV export started, you will receive an email once it is ready.'})

    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required(login_url='/')
def preview_data_view(request, project_name):
    if request.method == 'GET':
        fields_list = get_fields_from_request(request)
        model_cls = django_apps.get_model('tsepamo', project_name)
        data = list(model_cls.objects.values(*fields_list))
        return JsonResponse(data, safe=False)


def download_export_file_view(request, file_name):
    file_path = os.path.join(upload_folder, 'documents', file_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404("File does not exist")


def get_repository_details():
    records = []
    repository_data = ExportFile.objects.order_by('-date_created')
    for data in repository_data:
        records.append(
            {'name': data.name,
             'file_type': data.extension,
             'date_created': data.date_created.strftime('%Y-%m-%d %H:%M'),
             'user_created': data.user_badge,
             'file_status': data.export_status,
             'file_size': data.sizify,
             'actions': data.actions, })
    return records


def get_fields_from_request(request):
    selected_fields = request.GET.get('fields', '')
    fields_list = selected_fields.split(',')
    return fields_list


def get_fields_by_name(model_name):
    model_cls = django_apps.get_model('tsepamo', model_name)
    fields_tuple = model_cls._meta.fields
    return [{'name': field.name,
             'verbose_name': field.verbose_name,
             'instrument_name': model_name,
             'field_type': field.get_internal_type()} for field in fields_tuple if field.name not in exclude_fields]


def get_project_details(project_names=[]):
    details = []
    projects = get_projects_by_name(project_names)

    for project in projects:
        related_models = get_related_models_info(project)
        records_count = sum([related_info.get('records_count') for related_info in related_models])
        details.append({'name': project.name,
                        'id': project.id,
                        'verbose_name': project.verbose_name,
                        'instruments': len(related_models),
                        'records': records_count})
    return details


def get_forms_details(project_names=[]):
    details = []
    projects = get_projects_by_name(project_names)
    for project in projects:
        details.extend(get_related_models_info(project))
    return details


def get_project_columns():
    return [{'title': 'Project Name', 'data': 'verbose_name', },
            {'title': 'Project ID', 'data': 'id', },
            {'title': 'Records', 'data': 'records', },
            {'title': 'Instruments', 'data': 'instruments', }]


def get_forms_columns():
    return [{'title': 'Instrument Name', 'data': 'verbose_name', },
            {'title': 'Project Name', 'data': 'project_name', },
            {'title': 'Records', 'data': 'records_count', }]


def get_fields_columns():
    return [{'title': 'Verbose Field Name', 'data': 'verbose_name', },
            {'title': 'Variable Name', 'data': 'name', },
            {'title': 'Field Type', 'data': 'field_type', },
            {'title': 'Instrument Name', 'data': 'instrument_name', }]


def get_repository_columns():
    return [{'title': 'File Name', 'data': 'name', },
            {'title': 'File Type', 'data': 'file_type', },
            {'title': 'Created', 'data': 'date_created', },
            {'title': 'Created by', 'data': 'user_created', },
            {'title': 'Status', 'data': 'file_status', },
            {'title': 'Size', 'data': 'file_size', },
            {'title': 'Actions', 'data': 'actions', }]


def get_related_models_info(instance, app_label='tsepamo', ):
    """ Queries for model instances with relation to the provided
        project instance, and creates a dictionary with {model_name: records_count}
        @param instance: Projects instance
        @return: list of related_models and their records_count
    """
    related_models = []

    instruments_meta = InstrumentsMeta.objects.filter(
        related_project=instance.name).values_list('form_name', flat=True)
    for model_name in instruments_meta:
        related_model_cls = django_apps.get_model(app_label, model_name)
        related_model_name = related_model_cls._meta.model_name
        records_count = get_record_count(related_model_cls)

        related_models.append(
            {'name': related_model_name,
             'project_name': instance.verbose_name,
             'verbose_name': related_model_cls._meta.verbose_name,
             'records_count': records_count})
    return related_models


def get_projects_by_name(project_names=[]):
    if project_names:
        return Projects.objects.filter(name__in=project_names)
    else:
        return Projects.objects.all()


def get_record_count(model_cls):
    return model_cls.objects.count()


def get_latest_export_file():
    try:
        latest_file = ExportFile.objects.latest('date_created')
    except ExportFile.DoesNotExist:
        return None
    else:
        return latest_file
