from django.contrib import admin
from .models import Todo
class new(admin.ModelAdmin):
    list_display = ('title','details','date')
admin.site.register(Todo,new)