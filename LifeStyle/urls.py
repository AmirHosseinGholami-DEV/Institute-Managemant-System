from django.urls import path
from . import views

urlpatterns = [
    path("", views.LifeStyleAbout.as_view(), name="Life Style"),
    path("register/", views.RegisterView.as_view(), name="Life Style Register")
]