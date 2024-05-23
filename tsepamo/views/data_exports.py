from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render

from ..models import Projects, InstrumentsMeta
from ..export_utils import GenerateDataExports


# @login_required(login_url='/')
def render_export_reports_page(request, project_names):

    # fields = Field.objects.filter(form__project__id__in=project_ids)
    data = [{'tab_item': 'projects',
             'table_columns': get_project_columns(),
             'table_id': 'projectsList',
             'data_url': 'tsepamo:projects-details',
             'url_kwargs': {}},
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


def render_projects_page(request):
    table_columns = get_project_columns()
    return render(
        request, 'tsepamo/projects.html', {'table_columns': table_columns})


def project_data_view(request):
    if request.method == 'GET':
        project_details = get_project_details()
        return JsonResponse(project_details, safe=False)


def form_data_view(request, project_names):
    if request.method == 'GET':
        project_names = project_names.split(',')
        form_details = get_forms_details(project_names)
        return JsonResponse(form_details, safe=False)


# @login_required(login_url='/')
def project_fields(request, project_name):
    model_cls = django_apps.get_model('tsepamo', project_name)
    fields_tuple = model_cls._meta.fields
    fields = [{'name': field.name, 'verbose_name': field.verbose_name} for field in fields_tuple]
    return JsonResponse(fields, safe=False)


# def fetch_fields(request):
#     form_ids = request.GET.get('form_ids', '').split(',')
#     fields = Field.objects.filter(form__id__in=form_ids)
#     fields_data = [{
#         'id': field.id,
#         'form_name': field.form.name,
#         'name': field.name,
#         'field_type': field.field_type
#     } for field in fields]
#     return JsonResponse({'fields': fields_data})


@login_required(login_url='/')
def export_view(request, project_name):
    if request.method == 'GET':
        fields_list = get_fields_from_request(request)
        gen_exports = GenerateDataExports('tsepamo', project_name, fields_list)
        response = gen_exports.export_as_csv()
        return response


@login_required(login_url='/')
def preview_data_view(request, project_name):
    if request.method == 'GET':
        fields_list = get_fields_from_request(request)
        model_cls = django_apps.get_model('tsepamo', project_name)
        data = list(model_cls.objects.values(*fields_list))
        return JsonResponse(data, safe=False)


def get_fields_from_request(request):
    selected_fields = request.GET.get('fields', '')
    fields_list = selected_fields.split(',')
    return fields_list


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
    return [{'title': 'Field Name', 'data': 'verbose_name', },
            {'title': 'Field Type', 'data': 'field_type', }]


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
            {'project_name': instance.verbose_name,
             'model_name': related_model_name,
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
