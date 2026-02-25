from django.contrib import admin
from .models import User, Assignment

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    search_fields = ['username']
    ordering = ['id']

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['assignment_id', 'username', 'assignment_name', 'submitted_status', 'submitted_time']
    list_filter = ['submitted_status', 'submitted_time']
    search_fields = ['assignment_name', 'username__username']
    ordering = ['-assignment_id']

admin.site.register(User, UserAdmin)
admin.site.register(Assignment, AssignmentAdmin)
