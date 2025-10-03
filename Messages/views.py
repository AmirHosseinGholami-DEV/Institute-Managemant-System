from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from .forms import DatabaseForm
from django.views.generic import TemplateView

class Contact_Submit(View):
    def get(self, request):
        form = DatabaseForm()
        return render(request, 'Contact/Contact.html', {'form': form})

    def post(self, request):
        form = DatabaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'Contact/Contact.html', {'form': form})

class SuccessView(View):
    def get(self, request):
        return render(request, 'Home.html')
