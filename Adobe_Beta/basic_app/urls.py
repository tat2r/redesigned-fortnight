from django.urls import path
from basic_app import views
from django.conf.urls import url 
from .views import(
	CustomerListView,
	CustomerDetailView
	)

app_name = 'basic_app'

urlpatterns = [
	path('relative/', views.relative, name='relative'),
	path('other/', views.other, name='other'),
	path('base/', views.base, name='base'),
	path('testimony/', views.testimony, name='testimony'),
	path('intake_form/', views.intake_form, name='intake_form'),
	path('index/', views.IndexView.as_view(), name='index'),
	path('shuttle/', views.shuttle, name='shuttle'),
	path('van_rental/', views.van_rental, name='van_rental'),
	path('customer_list/', views.CustomerListView.as_view(), name='list'),
	path('customer_list/<int:pk>/', views.CustomerDetailView.as_view(), name='detail'),
	path('driver_list/', views.DriverListView.as_view(), name='driver_list'),
	path('driver_list/<int:pk>/', views.DriverDetailView.as_view()),
	path('van_list/', views.VanListView.as_view(), name='van_list'),
	path('van_list/<int:pk>/', views.VanDetailView.as_view()),
]

