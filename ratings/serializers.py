from rest_framework import serializers
from ratings.models import MovieDetails,Genre


class GenreSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(required=False)

	class Meta:
		model = Genre
		fields = [

			'id',
			'genre_title'
		]
		read_only_fields =('moviedetails',)


class MovieDetailsSerializer(serializers.ModelSerializer):
	genre = GenreSerializer(many=True)

	class Meta:
		model = MovieDetails
		fields = [
			'id',
			'popularity',
			'director',
			'imdb_score',
			'movie_title',
			'genre'
		]

	def create(self,validate_data):
		genre = validate_data.pop('genre')
		moviedetails = MovieDetails.objects.create(**validate_data)
		for  i in genre:
			Genre.objects.create(**i,moviedetails=moviedetails)
		return moviedetails

	def update(self, instance, validated_data):
		genre = validated_data.pop('genre')
		instance.popularity = validated_data.get("popularity", instance.popularity)
		instance.director = validated_data.get("director", instance.director)
		instance.imdb_score = validated_data.get("imdb_score", instance.imdb_score)
		instance.movie_title = validated_data.get("movie_title", instance.movie_title)
		instance.save()

		keep_genre = []
		for i in genre:
		    if "id" in i.keys():
		        if Genre.objects.filter(id=i["id"]).exists():
		            g = Genre.objects.get(id=i["id"])
		            g.genre_title = i.get('genre_title', g.genre_title)
		            g.save()
		            keep_genre.append(g.id)
		        else:
		            continue
		    else:
		        g = Genre.objects.create(**i, moviedetails=instance)
		        keep_genre.append(g.id)

		for j in instance.genre:
		    if j.id not in keep_genre:
		        j.delete()
		return instance