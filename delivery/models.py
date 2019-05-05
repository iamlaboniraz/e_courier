from django.db import models
import datetime
from django.utils import timezone
from measurement.measures import Weight
from django_measurement.models import MeasurementField

class types_of_product(models.Model):
	title=models.CharField(max_length=100)
	def __str__(self):
		return self.title

class delivery_product(models.Model):
	to_location=models.CharField(max_length=100)
	from_location=models.CharField(max_length=100)
	product_type=models.ForeignKey(types_of_product,on_delete=models.CASCADE)
	weight = MeasurementField(measurement=Weight)
	Date=models.DateTimeField(default=timezone.now)
	image=models.ImageField(upload_to='images/')

class driver(models.Model):
	username=models.CharField(max_length=100)
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	contact_number=models.IntegerField()
	profile_picture=models.ImageField(upload_to='images/')
	Car_details=models.CharField(max_length=100)
	Car_models_number=models.CharField(max_length=100)

	def __str__(self):
		return self.Car_details

