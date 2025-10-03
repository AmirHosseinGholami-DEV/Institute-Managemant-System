from django.urls import path
from . import views

urlpatterns = [
    path("", views.RhetoricalAbout.as_view(), name="Rhetorical"),
    path("register/", views.RegisterView.as_view(), name="Rhetorical Register")
]