from django import template
from django.urls.base import reverse

register = template.Library()


@register.inclusion_tag('tsepamo/custom_table.html')
def render_datatable(data_url, columns, table_id='default', url_kwargs={},
                     show_checkbox=True, allow_select_all=True,
                     include_seach_panes=True, download_action=False):

    data_url = reverse(data_url, kwargs=url_kwargs) if data_url else ""
    return {
        'data_url': data_url,
        'columns': columns,
        'table_id': table_id,
        'show_checkbox': show_checkbox,
        'allow_select_all': allow_select_all,
        'download_action': download_action,
        'include_seach_panes': include_seach_panes}


@register.filter(name='construct_table_id')
def construct_table_id(value, unique_arg):
    return f'{value}{unique_arg}'


@register.filter(name='sizify')
def sizify(value):
    """
        Simple kb/mb/gb size snippet for templates:
        {{ product.file.size|sizify }}
    """

    if value < 512000:
        value = value / 1024.0
        ext = 'kb'
    elif value < 4194304000:
        value = value / 1048576.0
        ext = 'mb'
    else:
        value = value / 1073741824.0
        ext = 'gb'
    return '%s %s' % (str(round(value, 2)), ext)
