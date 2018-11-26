from django.urls import path, re_path
from . import views

#list of urls used in the journal module
urlpatterns = [
	path('', views.index, name ='index'),
    #path('create/', views.create, name='create'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('new_entry/submitted/', views.submitted, name='submitted'),
	path('new_entry/graph/<int:id>', views.graph, name='graph'),
	path('get_entry/', views.get_entry, name='get entry'),
	path('get_spec_entry/<int:timestamp>', views.get_spec_entry)
	# re_path(r'^get_entry/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.get_spec_entry, name='Get Entry'),
	# url(r'^get_entry/(?P<string>[\w\-]+)/$',views.get_entry)
]
