from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name ='index'),
    #path('create/', views.create, name='create'),
    path('get_entry/', views.get_entry, name='get_entry'),
    path('get_entry/submitted/', views.submitted, name='submitted')
]
