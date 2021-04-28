from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Apply)
class ApplyAdmin(admin.ModelAdmin):
    pass