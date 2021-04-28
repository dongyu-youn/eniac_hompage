from django import forms
from . import models

class StudyModelForm(forms.ModelForm):
    class Meta:
        model = models.Study
        fields = (
            "Study_Name",
            "Programing_Language",
            "Recruit_Member_Number",
            "Learning_Cycle",
            "Deadline_Date",
            "Introduce",
    
            "Image",
        )

        widgets = {
            "Study_Name": forms.TextInput(attrs={'placeholder': 'Enter your study name'}),
            "Recruit_Member_Number": forms.TextInput(attrs={'placeholder': '0'}),
            "Learning_Cycle": forms.TextInput(attrs={'placeholder': '주 2~ 3회 1~2시간씩'}),
            "Deadline_Date": forms.TextInput(attrs={'placeholder': '2022-04-25'}),
            "Introduce": forms.Textarea(attrs={'placeholder': 'Enter Introduce'}),
        }
