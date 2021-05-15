from django import forms
from . import models

class ApplyModelForm(forms.ModelForm):
    class Meta:
        model = models.Apply
        fields = (
            "name",
            "motivate",
            "introduce",
            "resolution",
            # "apply_user",
            # "apply_room", 
        )
        widgets = {
            "name": forms.TextInput(attrs={'placeholder': '이름'}),
            "motivate": forms.TextInput(attrs={'placeholder': '지원 동기'}),
            "introduce": forms.TextInput(attrs={'placeholder': '자기 소개, 본인 어필'}),
            "resolution": forms.Textarea(attrs={'placeholder': '각오 한 마디'}),
        }
    