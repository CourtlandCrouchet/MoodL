from django.urls import path
from . import views

#list of urls used in the journal module
urlpatterns = [
	path('', views.index, name ='index'),
    #path('create/', views.create, name='create'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('new_entry/submitted/', views.submitted, name='submitted'),
	path('new_entry/graph/<int:id>', views.graph, name='graph'),
	# path('get_entry/<slug:id>/<slug:date_str>', views.get_entry, name='Get Entry'),
	# url(r'^get_entry/(?P<string>[\w\-]+)/$',views.get_entry)
]
