from django.urls import path,include
from ratings.jobs import dump_data
from ratings.views import MovieManagerView,MovieListView


urlpatterns = [
	path('api/',MovieListView.as_view(),name="api"),
	path('api/<id>/',MovieManagerView.as_view(),name="api"),
	path('dump/',dump_data,name="dump_data"),    
]
