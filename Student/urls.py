from django.urls import path
from . import views

urlpatterns = [
    path("", views.Student_List, name="Student"),
]
