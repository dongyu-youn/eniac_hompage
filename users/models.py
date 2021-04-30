from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
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
    GRADE_A = "4학년"
    
    GRADE_CHOICES = (
        (GRADE_F, "1학년"),
        (GRADE_S, "2학년"),
        (GRADE_T, "3학년"),
        (GRADE_A, "4학년"),
    )
    
    email = models.CharField(max_length=70, null=True, blank=True)
    fav_pro_genre = models.CharField(choices=GENRE_CHOICES, max_length=20, blank=True, null=True)
    
    major = models.CharField(max_length=20, blank=True, null=True)
    grade = models.CharField(choices=GRADE_CHOICES, max_length=20, blank=True, null=True)
    entered_eniac = models.CharField(default=32, max_length=10)
    name = models.CharField(max_length=20)
    profile_image = models.ImageField()
    
    def get_absolute_url(self):
     
        return reverse("users:profile", kwargs={'pk': self.pk})

   
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=64)
    profile_photo = models.ImageField(blank=True)                 # 값을 채워넣지 않아도 되는 속성.
    