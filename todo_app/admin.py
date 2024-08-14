from django.contrib import admin
from .models import Tasks
# Register your models here.

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'done')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_filter = ('done',)
