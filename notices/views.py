from django.shortcuts import render
from django.views.generic import CreateView
from . import models as notices_models
# Create your views here.

def ConVeyNoticeView(request):
    sdasd = "sdasdad"
    notices = notices_models.objects.all()
    return (request, "partials/header.html", {
        "notices" : notices,
        "sdasd": sdasd,
    })