from django.urls import path
from . import views as notices_views

app_name = "notices"

urlpatterns = [
    path("", notices_views.ConVeyNoticeView, name="create"),
]