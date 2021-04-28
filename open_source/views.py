from django.shortcuts import render 
from users.models import User
from studies.models import Study
from open_source.models import OpenSource, OpenSourceReview
from django.views.generic import CreateView, UpdateView
from . import forms
from django.shortcuts import redirect
from . import models
from django.urls import reverse_lazy, reverse
from reviews.models import Review

# Create your views here.

def listview(request):
    opensources = OpenSource.objects.all().order_by('-created')
    # print(dir(OpenSource.objects.get(pk=34).code_Language))
    # print(OpenSource.objects.get(pk=32).code_Language.all())
    return render(request,"opensource/list.html", {"opensources": opensources})

def detailview(request, pk):
    review_users_and_reviews = []  
    reviews = Review.objects.select_related('OpenSource_host').filter(OpenSource_Room=pk)
    opensource = OpenSource.objects.get(pk=pk)
    user = User.objects.get(username=opensource.OpenSource_host)
    try: 
        study = Study.objects.get(Room_Host=user)
        return render(request, "opensource/detail.html", {
            "study": study,
            "user": user,
            "opensource": opensource,
            "reviews": reviews,
        })
    except:
        return render(request, "opensource/detail.html", {
        "user": user,
        "opensource": opensource,
        "reviews": reviews,
    })

class OpenSourceUpdateView(UpdateView):

    model = models.OpenSource
    template_name = "opensource/opensource_update.html"
    fields = (

        "title",
        "code_Language",
        "code",
        "explain_situation",
        "error",
    )

    def form_valid(self, form):
        opensource = form.save()
        opensource.error_signal = True
        opensource.save()
        return redirect(reverse("opensource:detail", kwargs={"pk": opensource.pk}))