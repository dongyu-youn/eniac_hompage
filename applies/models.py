from django.db import models
from core import models as core_models
from django.urls import reverse

# Create your models here.

class Apply(core_models.TimeStampedModel):
    
    name = models.CharField(max_length=80, null=True, blank=True)
    motivate = models.TextField(null=True, blank=True)
    introduce = models.TextField(null=True, blank=True)
    resolution = models.TextField(null=True, blank=True)
    apply_user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    apply_room = models.ForeignKey("studies.Study", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("studies:detail", kwargs={"pk": self.apply_room.pk})

