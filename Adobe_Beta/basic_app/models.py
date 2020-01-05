from django.db import models
import datetime
from django.utils import timezone

# Create your models here.



class Customer(models.Model):
	first_name = models.CharField(max_length=128, blank=False)
	last_name = models.CharField(max_length=128, blank=False)
	email = models.CharField(max_length=128, blank=True)
	cell_phone = models.CharField(max_length=20, blank=True)
	address = models.CharField(max_length=50, blank=True)
	# city = models.CharField(max_length=50, blank=True)
	# state = models.CharField(max_length=50, blank=True)
	# zip_code = models.CharField(max_length=20, blank=True)
	dl_num = models.CharField(max_length=50, blank=True)
	# dl_dob = models.DateField(blank=True)
	# dl_exp = models.DateField(blank=True)
	def __str__(self):
		return self.last_name+', '+self.first_name

class Van(models.Model):
	van_num = models.CharField(max_length=4, blank=True)
	vin = models.CharField(max_length=60, blank=True)
	year_make_model = models.CharField(max_length=128, blank=True)
	plate = models.CharField(max_length=10, blank=True)
	# tag_exp = models.CharField(max_length=12, blank=True)



	def __str__(self):
		return	self.van_num



# class VanRental(models.Model):
# 	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
# 	# rent_from = models.DateField()
# 	# rent_to = models.DateField()
# 	van_rented = models.ForeignKey(Van, related_name='van', on_delete=models.CASCADE)

class Driver(models.Model):
	first_name = models.CharField(max_length=128, blank=False)
	last_name = models.CharField(max_length=128, blank=False)
	email = models.CharField(max_length=128, blank=True)
	cell_phone = models.CharField(max_length=20, blank=True)
	address = models.CharField(max_length=50, blank=True)
	city = models.CharField(max_length=50, blank=True)
	state = models.CharField(max_length=50, blank=True)
	zip_code = models.CharField(max_length=20, blank=True)
	dl_num = models.CharField(max_length=50, blank=True)
	# dl_dob = models.DateField(blank=True)
	# dl_exp = models.DateField(blank=True)

	def __str__(self):
		return self.last_name+', '+self.first_name