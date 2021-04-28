from django.urls import path
from open_source.views import listview, detailview, OpenSourceUpdateView

app_name = "opensource"

urlpatterns = [
    path("opensource/", listview, name="list"),
    path("opensource/<int:pk>/", detailview, name="detail"),
    # path("opensource/reviewcreate/<int:room>", OpenSourceReviewView, name="reviewcreate"),
    path("opensource/<int:pk>/update/", OpenSourceUpdateView.as_view(), name="update"),
    ]