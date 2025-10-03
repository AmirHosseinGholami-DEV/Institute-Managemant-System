from django.urls import path
from . import views

urlpatterns = [
    path("", views.LogoAbout.as_view(), name="logo"),
    path("register/", views.RegisterView.as_view(), name="Logo Register")
]
