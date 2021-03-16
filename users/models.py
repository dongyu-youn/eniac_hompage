from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class User(AbstractUser):

    GENRE_WEB = "WEB"
    GENRE_APP = "APP"
    GENRE_AI = "AI"
    GENRE_GAME = "GAME"

    GENRE_CHOICES = (
      (GENRE_WEB, "WEB"),
      (GENRE_APP, "APP"),
      (GENRE_AI, "AI"),
      (GENRE_GAME, "GAME"),
    )

    GRADE_F = "1학년"
    GRADE_S = "2학년"
    GRADE_T = "3학년"
    
    GRADE_CHOICES = (
        (GRADE_F, "1학년"),
        (GRADE_S, "2학년"),
        (GRADE_T, "3학년"),
    )
    
    major = models.CharField(max_length=20, blank=True, null=True)
    fav_pro_genre = models.CharField(choices=GENRE_CHOICES, max_length=20, blank=True, null=True)
    grade = models.CharField(choices=GRADE_CHOICES, max_length=20, blank=True, null=True)
    
    