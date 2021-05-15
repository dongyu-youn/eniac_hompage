from django import forms
from . import models

class CreateLView(forms.ModelForm):
    class Meta:
        model = models.Lecture
        fields = (
            "title",
            "category",
            "link",
            "person",
            "image",
        )

        # widgets = {
        #    "title",
        #    "person",
        #    "image",
        #    "category"
        # }
