from django.http import HttpResponse,JsonResponse
import json
from ratings.models import MovieDetails,Genre

def dump_data(request):
	file = open('imdb.json',)
	data = json.loads(file.read())
	for i in data:
		try:
			movie_details = MovieDetails.objects.create(
				popularity = i['99popularity'],
				director = i['director'],
				imdb_score=i['imdb_score'],
				movie_title=i['name']
				)
			try:
				for j in i['genre']:
					Genre.objects.create(
						moviedetails_id = movie_details.id,
						genre_title = j
						)
			except:
				pass
		except:
			pass
	return HttpResponse("Added succesfully")


	