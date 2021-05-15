from django.http import Http404
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from . import models
from users.models import User
from django.views.generic.edit import FormView
from . import forms
from django.urls import reverse, reverse_lazy

# Create your views here.

def studiesview(request):

    check_list = request.GET.get("subject")
    study = models.Study.objects.all()
    language_list = models.LanguageType.objects.all()
    s_languages = request.GET.getlist("language")
    all_study = models.Study.objects.all()
    Deadline_False = all_study.filter(Deadline=False).count()
    Deadline_True = all_study.filter(Deadline=True).count()
    language_categori = request.GET.get("language_categori")

    if len(s_languages):
        study = study.filter(Programing_Language__name__in=s_languages,).distinct()
        # print("asdas")
        # print(dir(study[2].programing_language))
        # print(study[2].programing_language.__dict__)
    # if request.GET.getlist("reset") == 'True':
    #     study = models.Study.objects.all()
    if(check_list == "continue"):
        study = study.filter(Deadline=True)
    elif(check_list == "dead"):
        study = study.filter(Deadline=False)
    if language_categori:
        if(language_categori=="웹"):
            study = study.filter(study_genre="Web")
        elif(language_categori=="앱"):
            study = study.filter(study_genre="App")
        elif(language_categori=="인공지능"):
            study = study.filter(study_genre="Machine_Learning")
        elif(language_categori=="게임"):
            study = study.filter(study_genre="Game")
    return render(request,"studies/list.html", 
        {"list":language_list,
        "studies": study,
        "s_languages": s_languages,
        "all_study": all_study,
        "check_list": check_list,
        "Deadline_False": Deadline_False,
        "Deadline_True": Deadline_True,
        })

def studydetail(request, pk):
    
    study = models.Study.objects.get(pk=pk)
    host_inf = User.objects.get(username=study.Room_Host)
    room_members = study.Room_Member.all()
    print(request.POST.get('Recruitment_off'))
    if(request.POST.get('Recruitment_off')=="off"):
        study.Deadline = False
        study.save()
        print(1)
        print(study.Deadline)
    if(request.POST.get('Recruitment_on')=="on"):
        study.Deadline = True
        study.save()
        print(2)

    return render(request, "studies/study_detail.html",
                {
            'study': study,
            'host_inf': host_inf,
            'room_members': room_members,
        }
    )

class StudyUpdateView(UpdateView):
    
    model = models.Study
    template_name = "studies/study_update.html"
    fields = (
        "Study_Name",
        "Programing_Language",
        "Recruit_Member_Number",
        "Learning_Cycle",
        "Deadline_Date",
        "Introduce",
        "Room_Host",
    )

    def get_object(self, queryset=None):
        room = super().get_object(queryset=queryset)
        if room.Room_Host.pk != self.request.user.pk:
            return Http404
        else:
            return room

def applyview(request):
    return render(request, "studies/apply.html")

class StudyCreateView(CreateView):
    template_name = 'studies/study_create.html'
    form_class = forms.StudyModelForm
    queryset = models.Study.objects.all()

    def form_valid(self, form):
        study=form.save(commit=False)
        study.Room_Host = self.request.user
        study.Deadline = True
        study.Leader = self.request.user.name
        study.save()


        return super().form_valid(form)
