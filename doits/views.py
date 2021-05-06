from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.views.generic import ListView, DetailView, UpdateView, CreateView, FormView
from django.urls import reverse
from django.http import Http404
from . import forms
from doits.models import Doit

class DoitView(ListView):
    
   model = models.Doit
   paginate_by = 6
   ordering = "created" #정렬
   paginate_orphans = 5

   ordering = ['-updated']

def doitlistview(request):
   return render(request, "")



def doits_detail(request, pk):
   try:
      doit = models.Doit.objects.get(pk=pk)
      return render(request, "doits/doit_detail.html", {"doit": doit})
   except models.Price.DoesNotExist:
      raise Http404()   
   
   #doit : 제목 이미지 깃허브주소 장르







class DoitCreateView(CreateView):
    template_name = 'doits/doit_create.html'
    form_class = forms.CreateView
    queryset = models.Doit.objects.all()

    def form_valid(self, form):
      doit = form.save()
      doit.user = self.request.user
      doit.save()
      return super().form_valid(form)

class DoitEditView(UpdateView):
   
   model = models.Doit
   template_name = "doits/doit_edit.html"
   fields = (
      "title",
      "Programing_Language",
      "category",
      "image",
      "explain",
      "link",
      "개발자",
   )

   def get_object(self, queryset=None):
        room = super().get_object(queryset=queryset)
        if room.user.pk != self.request.user.pk:
            return Http404
        else:
            return room