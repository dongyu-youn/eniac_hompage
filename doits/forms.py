from django import forms
from . import models

class CreateView(forms.ModelForm):
    class Meta:
        model = models.Doit
        fields = (
            "title",
            "Programing_Language",
            "category",
            "image",
            "explain",
            "link",
            # "개발자",
          
            # "user",
        )

        widgets = {
            "title": forms.TextInput(attrs={'placeholder': '프로젝트 이름'}),          
            "explain": forms.TextInput(attrs={'placeholder': '간단한 설명을 적어주세요'}),
            "link ": forms.TextInput(attrs={'placeholder': '링크를 적어주세요'}),
            # "category": forms.ChoiceField(),
            # "user": forms.Textarea(attrs={'placeholder': 'Enter Introduce'}),
            # "Programing_Language": forms.TextInput(attrs={'placeholder': '개발 언어'}),

        }
