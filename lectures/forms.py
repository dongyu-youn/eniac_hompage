from django import forms
from . import models

class CreateLView(forms.ModelForm):
    class Meta:
        model = models.Lecture
        fields = (
            "title",
            "person",
            "image",
            "category",
        )

        # widgets = {
        #    "title",
        #    "person",
        #    "image",
        #    "category"
        # }
