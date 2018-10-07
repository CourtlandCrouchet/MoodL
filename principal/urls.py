from django.urls import path, include
from . import views


urlpatterns = [
	
	path('', views.main_base_view, name ='main_base'),
	path('login/', views.login, name ='login')

]