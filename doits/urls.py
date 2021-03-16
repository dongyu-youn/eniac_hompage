from django.urls import path
from doits import views as doits_view

app_name = "doits"

urlpatterns = [
    path("doit/<int:pk>", doits_view.doits_detail, name="detail")
]


