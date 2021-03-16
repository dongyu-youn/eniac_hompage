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


class Price(core_models.TimeStampedModel):

    CATE_F = "교내대회"
    CATE_T = "교외대회"

    CATE_CHOCIES = (
        (CATE_F, "교내대회"),
        (CATE_T, "교외대회"),
    )

    title = models.CharField(max_length=120) 
    year = models.DateTimeField()
    cover_image = models.ImageField()
    category = models.CharField(
        max_length=20, choices=CATE_CHOCIES)
    person = models.CharField(default="", max_length=20)

    def __str__(self):
      return self.title  


