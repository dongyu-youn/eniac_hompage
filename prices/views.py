from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.http import Http404
from django.core.paginator import Paginator
from prices.models import Price
from studies.models import Study
from lectures.models import Lecture
from doits.models import Doit

def PriceView(request):
 obj = Price.objects.all().order_by('-created')[:4]
 obj_t = Study.objects.all().order_by('-created')[:6]
 obj_l = Lecture.objects.all().order_by('-created')[:4]
 obj_d = Doit.objects.all().order_by('-created')[:3]
 return render(request, 'prices/price_list.html', {
     "studys" : obj_t,
     "prices" : obj, 
     "lectures" : obj_l,
     "doits" : obj_d,

 })


# def PriceView(request):
#     obj = Price.objects.all()
#     context = {
#         "obj":obj
#     }
#     return render(request, 'prices/price_list.html')




def price_detail(request, pk):
    try:
        price = models.Price.objects.get(pk=pk)
        return render(request, "prices/detail.html", {"price": price})
    except models.Price.DoesNotExist:
        raise Http404()


def first_photo(request):
    image = Price.object.all() #모든 이미지 오브젝트를 가져오겠다
    return render(request, 'prices/price_list.html', {'image':image}) #내가 원하는 이미지를 랜더 싴겠다

def price_penal(request):
    try:
        price = models.Price.objects.get()
        return render(request, "prices/price_penal.html", {"price": price})
    except models.Price.DoesNotExist:
        raise Http404()


class PenalView(ListView):

   model = models.Price
   paginate_by = 4
   ordering = "created" #정렬
   template_name = "prices/price_penal.html"
   paginate_orphans = 10

#패널뷰

class IntroView(ListView):

   model = models.Price
   paginate_by = 4
   ordering = "created" #정렬
   template_name = "prices/price_intro.html"
   paginate_orphans = 10    

#시작뷰


class ProgramView(ListView):

   model = models.Price
   paginate_by = 4
   ordering = "created" #정렬
   template_name = "prices/price_program.html"
   paginate_orphans = 10

#price_program 뷰

class CapView(ListView):

   model = models.Price
   paginate_by = 4
   ordering = "created" #정렬
   template_name = "prices/price_cap.html"
   paginate_orphans = 10

#capview 뷰 

