from django.contrib import admin
from dartboard.models import Choice

"""
@admin.register(Decision)
class DecisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'author',)
    list_filter = ('author',)
"""

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    list_filter = ('author',)
