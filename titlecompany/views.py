

from results.models import *
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView

from django import forms
# from forms import *

class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea,required=False)

    def send_email(self):
        send_mail(
            'Some one filled out the form at JW Consulting. ',
            'It is from: ' + self.cleaned_data['email'] + '.\n With name: ' + self.cleaned_data['name'] + '\n Here is the message:' + self.cleaned_data['message'] ,
            'kevin@samizdatcollective.com',
            ['kfwojton@gmail.com','john.wojton@gmail.com'],
            fail_silently=False,
            )
        # send email using the self.cleaned_data dictionary
        pass
class start(FormView):
    model = email_subscribers
    # fields = ['name']
    form_class = ContactForm
    success_url = '/thanks'
    template_name = "index.html"

    def form_valid(self, form):
        form.send_email()
        return super(start, self).form_valid(form)

class thanks(TemplateView):
    model = email_subscribers
    template_name = "thanks.html"
    success_url = '/thanks'
