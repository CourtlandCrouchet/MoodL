from django.urls import path
from . import views

app_name = 'principal'

urlpatterns = [
	
	path('', views.main_base_view, name ='main_base'),
	path('', views.login, name ='login')

]