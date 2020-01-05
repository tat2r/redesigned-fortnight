import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'Adobe_Beta.settings')

import django

django.setup()

from basic_app.models import Customer
from faker import Faker


fakegen = Faker()


def populate(N=500):
	for entry in range(N):
		fake_name = fakegen.name().split()
		fake_first_name = fake_name[0]
		fake_last_name = fake_name[1]
		fake_email = fakegen.email()
		fake_add = fakegen.address()
		fake_phone = fakegen.phone_number()
		fake_dl = fakegen.ein()

		## New Entry
		customer = Customer.objects.get_or_create(first_name = fake_first_name,
												last_name=fake_last_name,
												cell_phone=fake_phone,
												email=fake_email,
												address=fake_add,
												dl_num=fake_dl
												)
if __name__ == '__main__':
	print("populating databases")
	populate(250)
	print("complete")

# print(fakegen.address())


# first_name
# last_name
# email
# cell_phone
# address
# dl_num
	