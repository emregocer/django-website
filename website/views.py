from django.shortcuts import render
import datetime
from django.utils.timezone import now
from django.views.generic.base import TemplateView

def home(request):
    today = datetime.date.today()
    return render(request, "website/index.html", {'today':today, 'now':now()})

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")

class Home(TemplateView):
    template_name = "website/index.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)

        context['today'] = datetime.date.today()
        context['now'] = now()
        
        return context

class AboutUs(TemplateView):
	template_name = 'website/about-us.html'