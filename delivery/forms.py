from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

## -- from models -- ##
from .models import delivery_product,types_of_product
## ----

## -- for product delivery Form -- ##
class deliverForm(forms.ModelForm):
	class Meta:
		model=delivery_product
		fields=['to_location','from_location','product_type','image','weight','Date']
		labels={
		      'to_location':'To Location : ',
		      'from_location':'From Location : ',
		      'product_type' :'Product Type : ',
		      'weight':'Weight : ',
		      'image':'Product Picture :',
		      'Date':'Date :'
		     }

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	contact_number=forms.IntegerField()
	facebook_id=forms.CharField(max_length=50)
	class Meta:
		model=User
		fields=(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'contact_number',
            'facebook_id'
			)
	def save(self,commit=True):
		user=super(RegistrationForm,self).save(commit=False)
		user.first_name=self.cleaned_data['first_name']
		user.last_name=self.cleaned_data['last_name']
		user.email=self.cleaned_data['email']
		user.contact_number=self.cleaned_data['contact_number']
		user.facebook_id=self.cleaned_data['facebook_id']

		if commit:
			user.save()
		return user

