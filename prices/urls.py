from django.urls import path
from prices import views as prices_view
from django.conf.urls.static import static
from django.conf import settings

app_name = "prices"

urlpatterns = [
    path("<int:pk>/detail/", prices_view.price_detail, name="detail"),
    path("", prices_view.first_photo, name="img_list"),
    path("penal/", prices_view.PenalView.as_view(), name="penal"),
    path("intro/", prices_view.IntroView.as_view(), name="intro"),
    path("program/", prices_view.ProgramView.as_view(), name="program"),
    path("cap/", prices_view.CapView.as_view(), name="cap"),
  
    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



