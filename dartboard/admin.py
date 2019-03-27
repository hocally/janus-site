from django.contrib import admin
from dartboard.models import Choice

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'timestamp')
    list_filter = ('author',)
