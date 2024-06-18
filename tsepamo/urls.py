# app_name/urls.py

from django.conf import settings
from django.urls import path
from .views import (render_export_reports_page, project_fields, export_view,
                    preview_data_view, render_projects_page, render_repository_page,
                    project_data_view, form_data_view, fetch_fields_view, repository_data_view,
                    download_export_file_view, render_dashboard_page)

app_name = 'tsepamo'

navbar_links = [
    {
        'label': 'Dashboard',
        'url': '/tsepamo/dashboard/',
        'icon': 'fas fa-tachometer-alt fa-fw me-3'
    },
    {
        'label': 'Projects',
        'url': '/tsepamo/projects/',
        'icon': 'fas fa-regular fa-folder-open fa-fw me-3',
        # 'dropdown_links': [
        #     {'label': 'Data Exports', 'url': '/tsepamo/', 'icon': 'fa-solid fa-file-export'},
        #     {'label': 'Reports', 'url': '', 'icon': 'fa-solid fa-chart-line'},
        # ]
    },
    {
        'label': 'Reports',
        'url': settings.MERCURY_URL,
        'icon': 'fas fa-solid fa-chart-line fa-fw me-3'
    },
    {
        'label': 'Repository',
        'url': '/tsepamo/repository/',
        'icon': 'fas fa-solid fa-server fa-fw me-3'
    }
]

urlpatterns = [
    path('dashboard/', render_dashboard_page, name='tsepamo-dashboard'),

    path('projects/', render_projects_page, name='projects-list'),
    path('projects/details/', project_data_view, name='projects-details'),

    path('repository/', render_repository_page, name='repository'),
    path('repository/details/', repository_data_view, name='repository-details'),
    path('repository/download/<str:file_name>', download_export_file_view, name='download-file'),

    path('projects/details/<str:project_names>/', project_data_view, name='projects-details'),
    path('projects/exports/<str:project_names>/', render_export_reports_page, name='export-reports'),

    path('instruments/details/<str:project_names>/', form_data_view, name='instruments-details'),
    path('instruments/fields/<str:instrument_names>/', fetch_fields_view, name='fetch-fields'),

    path('fields/preview/', preview_data_view, name='preview-data'),

    path('api/projects/<str:project_name>/fields/', project_fields, name='project-fields'),
    path('api/exports/', export_view, name='generate-export'),
]
