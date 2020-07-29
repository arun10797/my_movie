from django.db import models
from django.contrib.auth.models import User

class MovieDetails(models.Model):
	created_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
	popularity = models.DecimalField(max_digits=19, decimal_places=10, blank=True)
	director = models.CharField(max_length=200,blank=True)
	imdb_score = models.DecimalField(max_digits=19, decimal_places=10, blank=True)
	movie_title = models.CharField(max_length=1000,blank=True)

	def __str__(self):
		return self.movie_title

	@property
	def genre(self):
		return self.genre_set.all()
	

class Genre(models.Model):
	moviedetails = models.ForeignKey(MovieDetails,on_delete=models.CASCADE)
	genre_title = models.CharField(max_length=1000,blank=True)

	def __str__(self):
		return self.genre_title