from django.db import models
from core import models as core_models
# Create your models here.

class Notice(core_models.TimeStampedModel):
    
    associated_name = models.CharField(max_length=20, null=True, blank=True)
    explain = models.TextField(null=True, blank=True)
    send_user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, blank=True, related_name="send_user")
    receive_user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, blank=True, related_name="receive_user")

    def __str__(self):
        return self.associated_name