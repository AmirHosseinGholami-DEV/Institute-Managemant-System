from django.views.generic import TemplateView
from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from .forms import DatabaseForm


class LogoAbout(TemplateView):
    template_name = 'Logo/Logo.html'

class RegisterView(View):
    def get(self, request):
        form = DatabaseForm()
        return render(request, 'Logo/Register.html', {'form': form})

    def post(self, request):
        form = DatabaseForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'Logo/Register.html', {'form': form})

class SuccessView(View):
    def get(self, request):
        return render(request, 'Home.html')

def person_list(request):
    persons = Person.objects.all()  # تمام اشخاص را از دیتابیس بگیر
    return render(request, 'Admin/Logo.html', {'persons': persons})