from django.urls import path
from . import views

#list of urls used in the journal module
urlpatterns = [
	path('', views.index, name ='index'),
    #path('create/', views.create, name='create'),
    path('get_entry/', views.get_entry, name='User Log'),
    path('get_entry/submitted/', views.submitted, name='submitted'),
	path('get_entry/graph/<int:id>', views.graph, name='graph')

]
