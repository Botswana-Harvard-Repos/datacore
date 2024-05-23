# app_name/urls.py

from django.urls import path
from .views import (render_export_reports_page, project_fields, export_view,
                    preview_data_view, render_projects_page, project_data_view,
                    form_data_view)

app_name = 'tsepamo'

navbar_links = [
    {
        'label': 'Dashboard',
        'url': '',
        'icon': ''
    },
    {
        'label': 'Projects',
        'url': '/tsepamo/projects/',
        'icon': '',
        # 'dropdown_links': [
        #     {'label': 'Data Exports', 'url': '/tsepamo/', 'icon': 'fa-solid fa-file-export'},
        #     {'label': 'Reports', 'url': '', 'icon': 'fa-solid fa-chart-line'},
        # ]
    }
]

urlpatterns = [
    path('projects/', render_projects_page, name='projects-list'),
    path('projects/details/', project_data_view, name='projects-details'),
    path('projects/exports/<str:project_names>/', render_export_reports_page, name='export-reports'),
    path('instruments/details/<str:project_names>/', form_data_view, name='instruments-details'),
    path('api/projects/<str:project_name>/fields/', project_fields, name='project-fields'),
    path('api/exports/<str:project_name>/', export_view, name='export-view'),
    path('api/preview/<str:project_name>/', preview_data_view, name='preview-data')
]
