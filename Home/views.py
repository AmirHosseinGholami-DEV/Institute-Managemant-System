from django.views.generic import TemplateView
from Teacher.models import Teacher


class HomeView(TemplateView):
    template_name = 'Home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = Teacher.objects.all()
        return context



class AboutView(TemplateView):
    template_name = "About.html"
