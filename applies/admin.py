from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Apply)
class ApplyAdmin(admin.ModelAdmin):
    list_display = ("name", "motivate", "introduce", "resolution", "apply_user", "apply_room",
    )