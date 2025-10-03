from django.views.generic import TemplateView
from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from .forms import DatabaseForm

class MentalHealthAbout(TemplateView):
    template_name = 'MentalHealth/MentalHealth.html'

class RegisterView(View):
    def get(self, request):
        form = DatabaseForm()
        return render(request, 'MentalHealth/Register.html', {'form': form})

    def post(self, request):
        form = DatabaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'MentalHealth/Register.html', {'form': form})

class SuccessView(View):
    def get(self, request):
        return render(request, 'Home.html')