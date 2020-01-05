import django_filters
from . import models


class CustomerInfoFilter(django_filters.FilterSet):

	class Meta:
		model = models.Customer
		fields = {
			'last_name':['icontains'],
			'email':['icontains'],
			'cell_phone':['icontains']
		}

class DriverInfoFilter(django_filters.FilterSet):

	class Meta:
		model = models.Driver
		fields = {
			'last_name':['icontains'],
			'email':['icontains'],
			'cell_phone':['icontains']
		}


class VanInfoFilter(django_filters.FilterSet):

	class Meta:
		model = models.Van
		fields = {
			'van_num':['icontains']
		}