from django import forms
from . import models

class OpenSourceModelForm(forms.ModelForm):
    class Meta:
        model = models.OpenSource
        fields = (
            "error",
            "explain_situation",
            "code",
            "code_Language",
            # "OpenSource_host",
        )

        widgets = {
            "error": forms.Textarea(attrs={'placeholder': 'blank'}),
        #     "explain_situation": forms.Textarea(attrs={'placeholder': 'blank'}),
        #     "code": forms.Textarea(attrs={'placeholder': 'blank'}),
        #     "OpenSource_host": forms.Textarea(attrs={'placeholder': 'blank'}),
        }

from django import forms
from . import models

class OpenSourceReiviewModelForm(forms.ModelForm):
    class Meta:
        model = models.OpenSourceReview
        fields = (
            "error",
            "explain_situation",
            "code",
            # "OpenSourceReview_indicated_host",
        )


# class StudyModelForm(forms.ModelForm):
#     class Meta:
#         model = models.Study
#         fields = (
#             "Study_Name",
#             "Programing_Language",
#             "Recruit_Member_Number",
#             "Learning_Cycle",
#             "Deadline_Date",
#             "Introduce",
#             "Room_Host",
#         )

#         widgets = {
#             "Study_Name": forms.TextInput(attrs={'placeholder': 'Enter your study name'}),
#             "Recruit_Member_Number": forms.TextInput(attrs={'placeholder': '0'}),
#             "Learning_Cycle": forms.TextInput(attrs={'placeholder': '주 2~ 3회 1~2시간씩'}),
#             "Deadline_Date": forms.TextInput(attrs={'placeholder': '2022-04-25'}),
#             "Introduce": forms.Textarea(attrs={'placeholder': 'Enter Introduce'}),
#         }