from django.urls import path, include
from . import views

app_name = 'principal'

urlpatterns = [
	
	path('', views.main_base_view, name='main_base'),
	path('login/', views.login, name='login'),
	path('signup/', views.signup.as_view(), name='signup'),
	path('about/', views.about, name='about')
]