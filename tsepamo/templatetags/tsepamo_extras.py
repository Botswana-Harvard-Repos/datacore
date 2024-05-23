from django import template
from django.urls.base import reverse

register = template.Library()


@register.inclusion_tag('tsepamo/custom_table.html')
def render_datatable(data_url, columns, table_id='default', url_kwargs={},
                     show_checkbox=True, include_seach_panes=True):

    data_url = reverse(data_url, kwargs=url_kwargs) if data_url else ""
    return {
        'data_url': data_url,
        'columns': columns,
        'table_id': table_id,
        'show_checkbox': show_checkbox,
        'include_seach_panes': include_seach_panes}


@register.filter(name='construct_table_id')
def construct_table_id(value, unique_arg):
    return f'{value}{unique_arg}'
