from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.http import Http404

class PriceView(ListView):
    
   model = models.Price
   paginate_by = 12
   ordering = "created" #정렬
   paginate_orphans = 5
   

def price_detail(request, pk):
   try:
      price = models.Price.objects.get(pk=pk)
      return render(request, "prices/detail.html", {"price": price})
   except models.Price.DoesNotExist:
      raise Http404()
