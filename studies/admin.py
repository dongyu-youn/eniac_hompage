from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.LanguageType)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Study)
class StudyAdmin(admin.ModelAdmin):
    
    list_display = ("Leader", "count_rooms","Deadline",)

    filter_horizontal = ("Programing_Language","Room_Member")

    def count_rooms(self, obj):
        return obj.Programing_Language.count()