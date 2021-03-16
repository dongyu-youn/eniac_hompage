from django.db import models
from core import models as core_models
# Create your models here.

"""
Here are the models you have to create:
- Movie:
  title ->제목
  year -> 날짜
  cover_image -> 사진
  category (ManyToMany => categories.Category) -> 카테고리(무슨대회인지)
"""


class Doit(core_models.TimeStampedModel):

    GRADE_F = "1학년"
    GRADE_S = "2학년"
    GRADE_T = "3학년"
    
    GRADE_CHOICES = (
        (GRADE_F, "1학년"),
        (GRADE_S, "2학년"),
        (GRADE_T, "3학년"),
    )

    title = models.CharField(max_length=120) 
    cover_image = models.ImageField()   
    category = models.CharField(    
       default="", max_length=20)
    fav_pro_genre = models.CharField(choices=GRADE_CHOICES, max_length=20, blank=True, null=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
      return self.title  

    def first_photo(self):
        photo = self.photos.all()[:1]
        return photo.file.url
