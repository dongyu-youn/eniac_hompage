from django.urls import path
from doits import views as doits_view
from lectures import views as lecture_view
from lectures import views as lectures_view_two
from lectures import views as lectures_view_three
from lectures import views as lectures_view_four
from lectures import views as lectures_view_five


app_name = "lecture"

urlpatterns = [
    path("lec/create/", lecture_view.LectureCreateView.as_view(), name="create"),
    path("lecture/<int:pk>/edit/", lecture_view.LectureEditView.as_view(), name="edit"),
    path("lecture/", lecture_view.lectureview, name="list"),
]


