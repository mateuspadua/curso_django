# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Question, Choice, Tag


class ChoiceInline(admin.TabularInline):  # StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                      {'fields': ['question_text']}),
        ('Tags para classificação', {'fields': ['tags']}),
        ('Date information',        {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    filter_horizontal = ['tags']


admin.site.register(Question, QuestionAdmin)


class TagAdmin(admin.ModelAdmin):
	pass


admin.site.register(Tag, TagAdmin)