from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.http import Http404

class DoitView(ListView):
    
   model = models.Doit
   paginate_by = 12
   ordering = "created" #정렬
   paginate_orphans = 4

def doits_detail(request, pk):
   try:
      doit = models.Doit.objects.get(pk=pk)
      return render(request, "doits/doit_detail.html", {"doit": doit})
   except models.Price.DoesNotExist:
      raise Http404()
   
