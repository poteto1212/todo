from django.contrib import admin
from .models import TodoModel

class TodoAdmin(admin.ModelAdmin):
    list_display=('title','content','pic')
    
admin.site.register(TodoModel,TodoAdmin)