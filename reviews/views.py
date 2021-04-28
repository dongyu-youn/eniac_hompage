from django.shortcuts import render
from open_source import models as opensource_models
from . import forms
from . import models
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.http import Http404
import json
from django.http import JsonResponse
from reviews.models import Review


# Create your views here.
# Create your views here.



class UpdateReviewView(UpdateView):
    
    model = models.Review
    template_name = "reviews/review_edit.html"
    # pk_url_kwarg = room.OpenSource_host.pk
    fields = (
        "code",
        "error",
        "explain_situation",
    )

    def get_object(self, queryset=None):
        room = super().get_object(queryset=queryset)
        if room.OpenSource_host.pk != self.request.user.pk:
            return Http404
        else:
            return room
    
    def form_valid(self, form):
        
        form.save()
        pk = self.kwargs.get("pk")
        a = Review.objects.get(pk=pk)
        pk = a.OpenSource_Room.pk
        return redirect(reverse("opensource:detail", kwargs={"pk": pk}))

class CreateReviewView(CreateView):
    template_name = 'reviews/review_create.html'
    form_class = forms.CraeteReviewForm
    queryset = models.Review.objects.all()
    # success_url = reverse_lazy("core:price")

    def form_valid(self, form):               
        if self.request.method == "POST":
            pk = self.kwargs.get("pk")
            OpenSource_host = opensource_models.OpenSource.objects.get(pk=pk)
            if not OpenSource_host:
                return redirect(reverse("price:home"))
            if form.is_valid():
                review = form.save()
              
                review.OpenSource_Room = OpenSource_host
                review.OpenSource_host = self.request.user
                print(review.OpenSource_host)
                print("하아")
                print(review.OpenSource_Room)
                review.save()
                # super().form_valid(form)
                return redirect(reverse("opensource:detail", kwargs={"pk": OpenSource_host.pk}))
        else:
            print(2)
            return render(request, "reviews/review_create.html")

    # def get_absolute_url(self):
    #     return reverse("opensource:detail", kwargs={"pk": self.kwargs.get("pk")})    
    


def createreview(request, pk):
    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        OpenSource_host = opensource_models.OpenSource.objects.get_or_none(pk=pk)
        if not OpenSource_host:
            return redirect(reverse("price:home"))
        if form.is_valid():
            review = form.save()
            review.room = OpenSource_host
            review.user = request.user
            review.save()
            print(1)
            return render(request, "reviews/review_create.html",
            kwargs={
                "pk": OpenSource_host.pk
            })
    else:
        print(2)
        return render(request, "reviews/review_create.html")