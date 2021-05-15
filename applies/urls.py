from django.urls import path
from . import views

app_name="applies"

urlpatterns = [
    path("applies/create/<int:pk>", views.CreateApplyView.as_view(), name="create"),
    path("applies/list/<int:pk>/", views.applieslist, name="list"),
]