from django.urls import path
from prices import views as prices_view

app_name = "prices"

urlpatterns = [
    path("<int:pk>", prices_view.price_detail, name="detail")
]


