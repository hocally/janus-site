from django.contrib import admin
from dartboard.models import Choice, Decision

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'decision', 'author')
    list_filter = ('author',)

@admin.register(Decision)
class DecisionAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'author',)
    list_filter = ('author',)
