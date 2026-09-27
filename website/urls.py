from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
 	path('my_ajax_view/', views.my_ajax_view, name='my_ajax_view'),
]
	