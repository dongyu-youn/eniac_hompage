from django import forms
from . import models

class ApplyModelForm(forms.ModelForm):
    class Meta:
        model = models.Apply
        fields = (
            "Motive",
            "introduce",
            # "Apply_room",
            # "Apply_host",
        )