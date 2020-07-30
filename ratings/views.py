from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from ratings.models import MovieDetails,Genre
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from ratings.serializers import MovieDetailsSerializer,GenreSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication,BasicAuthentication 
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend


class MovieManagerView(
	generics.GenericAPIView,
	mixins.ListModelMixin,
	mixins.RetrieveModelMixin,
	mixins.UpdateModelMixin,
	mixins.DestroyModelMixin):

	serializer_class = MovieDetailsSerializer
	queryset = MovieDetails.objects.all()
	lookup_field = 'id'
	authentication_classes = [SessionAuthentication,BasicAuthentication]
	# permission_classes =[IsAuthenticated]

	def get(self,request,id=None):
		if id:
			return self.retrieve(request,id)
		else:
			return self.list(request)
	# @permission_classes([IsAuthenticated])
	# def post(self,request):
	# 	return self.create(request)

	@permission_classes([IsAuthenticated])
	def put(self,request,id=None):
		return self.update(request,id)
	@permission_classes([IsAuthenticated])
	def delete(self,request,id=None):
		return self.destroy(request,id)


class MovieListView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
	serializer_class = MovieDetailsSerializer
	queryset = MovieDetails.objects.all()
	# lookup_field = 'id'
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('popularity','director','imdb_score','movie_title','genre__genre_title',)	

	def get(self,request):
		return self.list(request)

	@permission_classes([IsAuthenticated])
	def post(self,request):
		return self.create(request)