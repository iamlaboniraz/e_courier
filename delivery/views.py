from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .forms import deliverForm
from .models import delivery_product,types_of_product,driver
from django.forms import formset_factory
from django.core.mail import send_mail
def first_page(request):
	return render(request,'first_page.html')

def home(request):
	return render(request,'home.html')

def signup(request):
	return render(request,'registration/signup.html')

def admin_account(request):
	return render(request,'registration/admin_account.html')

def personal_account(request):
	if request.method=="POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form=RegistrationForm()
	return render(request,'registration/personal_account.html',{'form':form})

def delivery_request(request):
	if request.method == 'POST':
		form_delivery=deliverForm(request.POST,request.FILES)
		if form_delivery.is_valid():
			form_delivery.save()
			# note = "Thanks for your request!! Wait a few minutes!! Car is on the way!!"
			new_form_delivery=deliverForm()
			return render(request,'delivery_form.html',{'deliveryform':new_form_delivery,})
	else:
		form_delivery = deliverForm()
		return render(request,'delivery_form.html',{'deliveryform':form_delivery})

def send_driver(request):
	driver_list=driver.objects.all()
	context ={
	 'driver_list':driver_list,
	}
	return render(request,'driver.html',context)


def confirm(request):
	return render(request,'confirm_massage.html')
