from django.urls import path
from . import views

app_name="applies"

urlpatterns = [
    path("studies/<int:pk>/apply", views.StudyApplyView.as_view(), name="create")
]