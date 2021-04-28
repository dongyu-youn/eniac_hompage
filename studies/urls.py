from django.urls import path
from studies import views as studies_view, models

app_name = "studies"

urlpatterns = [
    path("studies/", studies_view.studiesview, name="list"),
    path("studies/<int:pk>/", studies_view.studydetail, name="detail"),
    path("studies_create/", studies_view.StudyCreateView.as_view(), name="create"),
    path("studie/<int:pk>/edit/",studies_view.StudyUpdateView.as_view(), name="update"),
]