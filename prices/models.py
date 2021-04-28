from django.db import models
from core import models as core_models
from django.shortcuts import render
from PIL import Image 


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
    image = models.ImageField()
    category = models.CharField(
        max_length=20, choices=CATE_CHOCIES)
    person = models.CharField(default="", max_length=20)

    def save(self):
        super().save()  # 이미지저장

        img = Image.open(self.image.path) # 이미지 오픈

        if img.height > 280 or img.width > 280:
            new_img = (280, 280)
            img.thumbnail(new_img)
            img.save(self.image.path)  # 같은경로로 이미지 저장

    def __str__(self):
      return self.title

   
  

#업데이트




