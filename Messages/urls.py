from django.urls import path
from . import views

urlpatterns = [
    path("", views.Contact_Submit.as_view(), name="Contact"),
]
