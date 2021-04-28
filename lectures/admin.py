from django.contrib import admin
from lectures.models import Lecture
# Register your models here.

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):

    pass