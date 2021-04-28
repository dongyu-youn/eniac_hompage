from django.db import models
from core import models as core_models
from django.urls import reverse

# Create your models here.


class AbstractItem(core_models.TimeStampedModel):

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name 

class OpenSourceReview(AbstractItem):
    
    name = models.CharField(max_length = 20)
    error = models.TextField()
    explain_situation = models.TextField()
    code = models.TextField()
    # OpenSourceReview_indicated_host = models.ForeignKey("open_source.OpenSource", on_delete = models.CASCADE) 
    OpenSourceReview_host = models.ForeignKey("users.User", blank=True, null=True, on_delete = models.CASCADE)
    
    class Meta:
        verbose_name_plural = "OpenSourceReview"
    
    def get_absolute_url(self):
        return reverse("opensource:detail", kwargs={"pk": self.pk})

class OpenSource(core_models.TimeStampedModel):
    
    title = models.CharField(default="", max_length=40)
    error = models.TextField()
    explain_situation = models.TextField()
    code = models.TextField()
    code_Language = models.ManyToManyField("studies.LanguageType", related_name="code_language")
    OpenSource_host = models.ForeignKey("users.User", blank=True, null=True, on_delete = models.CASCADE)
    OpenSource_host_review = models.ManyToManyField("open_source.OpenSourceReview")
    error_signal = models.BooleanField(default="False")

    def get_absolute_url(self):
        return reverse("opensource:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.error