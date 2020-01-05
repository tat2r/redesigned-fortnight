from django import forms
from basic_app.models import Customer

class NewCustomerForm(forms.ModelForm):
	
	class Meta():
		model = Customer
		fields = '__all__'

		def clean(self):
			all_clean_data = super().clean()

			first_name = all_clean_data['first_name']
			last_name = all_clean_data['last_name']
			email = all_clean_data['email']
			cell_phone = all_clean_data['cell_phone']
			address = all_clean_data['address']
		