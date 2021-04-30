from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse
from django.http import Http404
from lectures.models import Lecture
from . import forms
from django.urls import reverse_lazy
from django.core.paginator import Paginator



# class LectureView(ListView):
    
#    model = models.Lecture
#    queryset = models.Lecture.objects.order_by('-created')

def lectureview(request):
    page = request.GET.get("page")
    lectures = models.Lecture.objects.all()
    paginator = Paginator(lectures, 10)
    lecture = paginator.get_page(page) 
    genre = request.POST.get("classify_genre")



    print(genre)
    if(genre == None or genre == all):
        print("pass")
        pass
    elif(genre == "web"):
        lectures = models.Lecture.objects.filter(category="웹")
    elif(genre == "machine_learning"):
        lectures = models.Lecture.objects.filter(category="인공지능")
    elif(genre == "game"):
        lectures = models.Lecture.objects.filter(category="게임")
    elif(genre == "app"):
        lectures = models.Lecture.objects.filter(category="앱")
    elif(genre == "whatever"):
        lectures = models.Lecture.objects.filter(category="그외")
    return render(request, "lectures/lecture_list.html", {"lectures": lectures})

class LectureCreateView(CreateView):
    template_name = 'lectures/lecture_create.html'
    form_class = forms.CreateLView
    queryset = models.Lecture.objects.all()

    def form_valid(self, form):
        lecture = form.save(commit=False)
        lecture.user = self.request.user
        lecture.save()
        return super().form_valid(form)	
        # lecture = form.save()
       
        # print(lecture.category)
        # if lecture.category == "웹":
        #     return(reverse("lecture:detail") )

class LectureEditView(UpdateView):

    model = models.Lecture
    template_name = "lectures/lecture_edit.html"
    fields = (
        "title",
        "person",
        "image",
        "category",
    )

    def get_object(self, queryset=None):
            room = super().get_object(queryset=queryset)
            if room.user.pk != self.request.user.pk:
                return Http404
            else:
                return room


# def lecture_detail_major(request):

#     lectures = Lecture.objects.filter(category="그외")
#     paginator = Paginator(lectures, 4)
#     page = request.GET.get('page')
#     posts = paginator.get_page(page)
#     return render(request, "lectures/major.html", {"lectures": lectures, "posts": posts})

# def lecture_detail_two(request):

#       lecture = models.Lecture.objects.all()
#       return render(request, "lectures/lecture_detail.html", {"lecture": lecture})

# def lecture_detail_three(request):

#       lecture = models.Lecture.objects.all()
#       return render(request, "lectures/lecture_detail.html", {"lecture": lecture})

# def lecture_detail_four(request):

#       lecture = models.Lecture.objects.all()
#       return render(request, "lectures/lecture_detail.html", {"lecture": lecture})


# def lecture_detail_five(request):

#       lecture = models.Lecture.objects.all()
#       return render(request, "lectures/lecture_detail.html", {"lecture": lecture})
 
   