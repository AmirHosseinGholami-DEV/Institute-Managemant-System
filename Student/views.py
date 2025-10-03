from django.views.generic import TemplateView
from django.views import View
from Admin.models import Student_Database
from django.shortcuts import render

def Student_List(request):
    contacts = Student_Database.objects.all()
    return render(request, 'Student/Student.html', {'contacts': contacts})