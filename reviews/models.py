from django.db import models
from core import models as core_models
from open_source import models as opensource_models
from users import models as users_models
from django.urls import reverse

# Create your models here.

class Review(core_models.TimeStampedModel):
    code = models.TextField() 
    OpenSource_Room = models.ForeignKey("open_source.OpenSource",null=True, blank=True, on_delete=models.CASCADE)
    OpenSource_host = models.ForeignKey("users.User",null=True, blank=True, on_delete=models.CASCADE)
    error = models.TextField()
    explain_situation = models.TextField()

    def get_absolute_url(self):
        return reverse("opensource:detail", kwargs={"pk": self.pk})
