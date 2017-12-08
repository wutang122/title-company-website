from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
        

class account_form(forms.Form):
	firstname = forms.CharField(label='First Name', required=False)
	lastname = forms.CharField(label='Last Name', required=False)
	address = forms.CharField(label='Address', required=False)
	zipcode = forms.CharField(label='Zipcode', required=False)
	City = forms.CharField(label='City', required=False)

class signin_form(forms.Form):
    username = forms.CharField(label='User Name', required=False)
    password = forms.CharField(label='Password', required=False)



class contact_us_form(forms.Form):
	firstname = forms.CharField(label='First Name', required=False)
	lastname = forms.CharField(label='Last Name', required=False)
	phone_number = forms.CharField(label='Phone Number', required=False)
	citya = forms.CharField(label='Order Number', required=False)
	city = forms.CharField(label='Email Address', required=False)
	message = forms.CharField(label='Message', required=False,widget=forms.Textarea(attrs={'cols':25, 'rows': 4}))
