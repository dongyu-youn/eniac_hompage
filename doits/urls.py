from django.urls import path
from doits import views as doits_view

app_name = "doit"

urlpatterns = [
    path("doit/", doits_view.doitlistview, name="list"),
    path("create/", doits_view.DoitCreateView.as_view(), name="create"),
    path("doit/<int:pk>/Edit", doits_view.DoitEditView.as_view(), name="edit"),
]


