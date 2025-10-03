from django.urls import path
from . import views

urlpatterns = [
    path("", views.MentalHealthAbout.as_view(), name="MentalHealth"),
    path("register/", views.RegisterView.as_view(), name="MentalHealth Register")
]
