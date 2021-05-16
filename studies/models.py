from django.db import models
from core import models as core_models
from django.urls import reverse
from users.models import User

# Create your models here.

class AbstractItem(core_models.TimeStampedModel):
    name = models.CharField(max_length = 20)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name 


class LanguageType(AbstractItem):
    
    class Meta:
        verbose_name_plural = "LanguageType"


Web = "Web"
App = "App"
AI = "AI"
game = "Game"
major = "major"

STUDY_GENRE_CHOICES = (
    ("Web", Web),
    ("App", App),
    ("AI", AI),
    ("Game", game),
    ("major", major),
)

class Study(core_models.TimeStampedModel):

    study_genre = models.CharField(choices=STUDY_GENRE_CHOICES, max_length=79, blank=True, null=True)
    Study_Name = models.CharField(max_length=70)
    Leader = models.CharField(max_length=70)
    Recruit_Member_Number = models.IntegerField()
    Programing_Language = models.ManyToManyField("studies.LanguageType", related_name="language",blank=True)
    Deadline = models.BooleanField(default=False)
    Title_Intro = models.TextField(null=True, blank=True)
    Introduce = models.TextField(null=True, blank=True)
    Learning_Cycle = models.CharField(max_length=70, null=True, blank=True)
    # Deadline_Date = models.DateField(blank=True, null=True)
    Room_Host = models.ForeignKey("users.User", on_delete = models.CASCADE)
    Room_Member = models.ManyToManyField("users.User", related_name="member" )
    Image = models.ImageField()
    
    @property
    def get_photo_url(self):
        if self.Image:
            return self.Image.url
        else:
            return "/static/images/user.jpg"

    def get_absolute_url(self):
        return reverse("studies:detail")

    def __str__(self):
        return self.Leader  

    def get_absolute_url(self):
        return reverse("studies:detail", kwargs={"pk": self.pk})


