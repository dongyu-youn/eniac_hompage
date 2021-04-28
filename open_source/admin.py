from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.OpenSourceReview)
class OpenSourceReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(models.OpenSource)
class OpenSourceAdmin(admin.ModelAdmin):
    pass