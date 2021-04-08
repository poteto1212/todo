from django.contrib import admin
from .models import TodoModel,SubjectModel,Field

class TodoAdmin(admin.ModelAdmin):
    list_display=('subject','title','content','pic')
admin.site.register(TodoModel,TodoAdmin)
    
class SubjectAdmin(admin.ModelAdmin):
    list_display=('subjects',)

admin.site.register(SubjectModel,SubjectAdmin)

admin.site.register(Field)