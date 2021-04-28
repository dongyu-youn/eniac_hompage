from django import forms
from . import models

class CraeteReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = (
            "error",
            "code",
            "explain_situation",
            # "OpenSource_Room",
            # "OpenSource_host",
        )

        def save(self):
            review = super().save(commit=False)
            return review