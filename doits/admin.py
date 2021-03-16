from django.contrib import admin
from doits.models import Doit
# Register your models here.

@admin.register(Doit)
class DoitAdmin(admin.ModelAdmin):

    pass