# -*- coding: utf-8 -*-
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget


class AdminImageWidget(AdminFileWidget):
    """
    A ImageField Widget for admin that shows a thumbnail.
    """

    def __init__(self, attrs={}):
        super(AdminImageWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "url"):
            output.append(('<div style="float:left; margin-right:10px; min-width:100px;"><a target="_blank" href="{0}">'
                           '<img src="{1}" style="max-height: 100px;" /></a></div> '.format(value.url, value.url)))
        output.append(super(AdminImageWidget, self).render(name, value, attrs))
        output.append('<span style="clear:both;"></span>')
        return mark_safe(u''.join(output))
