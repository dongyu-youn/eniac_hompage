from django.urls import path
from . import views as review_view

app_name = "reviews"

urlpatterns = [
    path("<int:pk>/review_create/", review_view.CreateReviewView.as_view(), name="create"),
    path("<int:pk>/review_edit/", review_view.UpdateReviewView.as_view(), name="edit"),
]