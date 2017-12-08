

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

    # def form_valid(self, form):
    #
    #     # form.send_email()
    #     return super(start, self).form_valid(form)

class thanks(TemplateView):
    model = email_subscribers
    template_name = "thanks.html"
    success_url = '/thanks'


class community(CreateView):
    template_name = "community.html"
    success_url = '/thanks'
    model = email_subscribers

class technology(CreateView):
    template_name = "technology.html"
    success_url = '/thanks'
    model = email_subscribers

class wellness(CreateView):
    template_name = "wellness.html"
    success_url = '/thanks'
    model = email_subscribers