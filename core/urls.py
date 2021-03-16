from django.urls import path
from prices import views as prices_view
from doits import views as doits_view



app_name = "core"

urlpatterns = [
    path("", prices_view.PriceView.as_view(), name="price"),
    path("doit/", doits_view.DoitView.as_view(), name="doit"),

]