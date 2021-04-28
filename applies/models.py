from django.db import models
from core import models as core_models
from django.urls import reverse
# Create your models here.

class Apply(core_models.TimeStampedModel):
    
    Motive = models.TextField(default="1")
    introduce = models.TextField(default="1")
    Apply_room = models.ForeignKey("studies.Study", null=True, blank=True, on_delete=models.CASCADE)
    Apply_host = models.ForeignKey("users.user", null=True, blank=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("studies:detail", kwargs={"pk":self.pk})

