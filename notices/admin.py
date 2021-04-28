from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Notice)
class NoticeAdmin(admin.ModelAdmin):
    pass