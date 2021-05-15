from django.db import models
from core import models as core_models
from django.urls import reverse
# Create your models here.

"""
Here are the models you have to create:
- Movie:
  title ->제목
  person -> 선생님
  cover_image -> 사진
  category (ManyToMany => categories.Category) -> 카테고리(무슨강의인지)
"""


class Lecture(core_models.TimeStampedModel):

    GENRE_WEB = "웹"
    GENRE_APP = "앱"
    GENRE_AI = "인공지능"
    GENRE_GAME = "게임"
    GENRE_OTHER = "그외"

    GENRE_CHOICES = (  
      (GENRE_WEB, "웹"),
      (GENRE_APP, "앱"),
      (GENRE_AI, "인공지능"),
      (GENRE_GAME, "게임"),
      (GENRE_OTHER, "그외"),
    )

    title = models.CharField(max_length=120) 
    person = models.CharField(max_length=20)
    image = models.ImageField()
    category = models.CharField(max_length=20, choices=GENRE_CHOICES)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, blank=True)
    link = models.URLField(max_length=70, )

    def __str__(self):
      return self.title  

    def get_absolute_url(self): # new
        return(reverse("lecture:detail") )

    class Meta:
      ordering = ['-created']

    @property
    def get_photo_url(self):
        if self.image:
            return self.image.url
        else:
            return "/static/images/user.jpg"
