from rest_framework.exceptions import ValidationError
# import django_filters.rest_framework
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


from delivery.serializers import DriverSerializers
from delivery.models import driver

class DriverList(ListAPIView):
	queryset=driver.objects.all()
	serializer_class = DriverSerializers
	filter_backends = (DjangoFilterBackend,SearchFilter)
	filter_fields=('id',)
	search_fields = ('Car_details','Car_models_number')

# for create
class DriverCreate(CreateAPIView):
	queryset=driver.objects.all()
	serializer_class = DriverSerializers


# for delete
class DriverDestroy(DestroyAPIView):
	queryset=driver.objects.all()
	lookup_field='id'
	def delete(self,request,*args,**kwargs):
		driver_id=request.data.get('id')
		response=super().delete(request,*args,**kwargs)
		if response.status_code==204:
			from django.core.cache import cache
			cache.delete('driver_data_{}'.format(driver_id))
		return response

# for update/delete
class DriverRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
	queryset=driver.objects.all()
	lookup_field='id'
	serializer_class=DriverSerializers

	def delete(self,request,*args,**kwargs):
		driver_id=request.data.get('id')
		response=super().delete(request,*args,**kwargs)
		if response.status_code==204:
			from django.core.cache import cache
			cache.delete('driver_data_{}'.format(driver_id))
		return response

	def update(self,request,*args,**kwargs):
		response=super().update(request,*args,**kwargs)
		if response.status_code==200:
			from django.core.cache import cache
			driver = response.data
			cache.set('driver_data_{}'.format(driver['id']),
                 {
                 'username':driver['username'],
                 'first_name':driver['first_name'],
                 'last_name':driver['last_name'],
                 'Car_details':driver['Car_details'],
                 'Car_models_number':driver['Car_models_number'],
                 'profile_picture':driver['profile_picture'],
                 
                 })
			return response
