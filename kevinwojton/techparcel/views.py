

from results.models import *

from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView

from django import forms
from forms import *



class start(CreateView):
    model = email_subscribers
    # fields = ['name']

    success_url = '/thanks'
    template_name = "index.html"

    def form_valid(self, form):

        # form.send_email()
        return super(start, self).form_valid(form)

class thanks(TemplateView):
    template_name = "thanks.html"

class community(TemplateView):
    template_name = "community.html"

class technology(TemplateView):
    template_name = "technology.html"

class wellness(TemplateView):
    template_name = "wellness.html"
