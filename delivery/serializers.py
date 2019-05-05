import rest_framework

from rest_framework import serializers
from delivery.models import driver
class DriverSerializers(serializers.ModelSerializer):
	class Meta:
		model=driver
		fields=('id',
			'username',
			'first_name',
			'last_name',
			'Car_details',
			'Car_models_number',
			'profile_picture')
