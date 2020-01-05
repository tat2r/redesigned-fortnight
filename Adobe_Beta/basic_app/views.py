from django.shortcuts import render
from .forms import NewCustomerForm
from . import models
from django.views.generic import View, TemplateView, ListView, DetailView
from .filters import CustomerInfoFilter, DriverInfoFilter, VanInfoFilter
# from django.views.generic.detail import DetailView
# Create your views here.


class IndexView(TemplateView):
	template_name = 'basic_app/index.html'

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['injectme'] = 'Basic Injection'
	# 	return context

## Edit the following filter to use date events for MAIN DISPLAY OUT

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['filter'] = CustomerInfoFilter(self.request.GET, queryset= self.get_queryset())
	# 	return context

class DriverListView(ListView):#(ListView):
	context_object_name = 'driver_list'
	model = models.Driver

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = DriverInfoFilter(self.request.GET, queryset= self.get_queryset())
		return context

class DriverDetailView(DetailView):
	context_object_name = 'driver_detail'
	model = models.Driver
	template_name = 'basic_app/driver_detail.html'





class CustomerListView(ListView):
	context_object_name = 'cust_list'
	model = models.Customer

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = CustomerInfoFilter(self.request.GET, queryset= self.get_queryset())
		return context

class CustomerDetailView(DetailView):
	context_object_name = 'customer_detail'
	model = models.Customer
	template_name = 'basic_app/customer_detail.html'



class VanListView(ListView):
	context_object_name = 'van_list'
	model = models.Van

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = VanInfoFilter(self.request.GET, queryset= self.get_queryset())
		return context

class VanDetailView(DetailView):
	context_object_name = 'van_detail'
	model = models.Van
	template_name = 'basic_app/van_detail.html'

# class index(View):
# 	def get(self, request):
# 		return	HttpResponse("Class Based Biews are Cool")


# def index(request):


# 	question_01 = 'Do you know Jesus Christ as your personal Lord and Savior?'
# 	context_dict = {'text':question_01, 'number':200}
# 	return render(request, 'basic_app/index.html', context_dict)





def other(request):
	return render(request, 'basic_app/other.html')

def relative(request):
	return render(request, 'basic_app/relative_url_templates.html')

def base(request):
	return render(request, 'basic_app/base.html')


def shuttle(request):
	return render(request, 'basic_app/shuttle.html')

def van_rental(request):
	return render(request, 'basic_app/van_rental.html')


def testimony(request):
	q1_dict = {'more_text':'this is more text'}
	return render(request, 'basic_app/testimony.html', q1_dict)

# def customer_list(request):

# 	c_list = Customer.objects.order_by('last_name')
# 	return render(request, 'basic_app/customer_list.html', {'customer_list':c_list})


def intake_form(request):
	form = NewCustomerForm()
	if request.method == "POST":
		form = NewCustomerForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			# return index(request)
		else:
			print('ERROR! FORM INVALID!!')

	return render(request, 'basic_app/intake_form.html', {'form':form})