from django.urls import path
from prices import views as prices_view
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "users"

urlpatterns = [
        path("login/", views.LoginView.as_view(), name="login"),
        path("signup/", views.SignUpView.as_view(), name="signup"),
        path("logout/", views.log_out, name="logout"),
        path("<int:pk>/", views.ProfielView.as_view(), name="profile"),

]


