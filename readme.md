# Movie Manager

Movie Manager is a simple rest api where it just create a movie record with its ratings,popularities and genre.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages used in project.

```bash
pip3 install -requirements.txt
```

## How to use api 
1) List all the movies with details (Authentication not required) 

```python
https://imdb-task-arun.herokuapp.com/
execute first GET method. 
```
If you want to access specific movie add id after url
```python
eg. https://imdb-task-arun.herokuapp.com/api/1/{GET}

```

2) make sure you authorize yourself with basic authentication with following details 
```python
username: arun
password:arun7666

```
2) Create Movies & details (User Authentication required)
```python

https://imdb-task-arun.herokuapp.com/api/1/{POST}

```
smaple input data
```json

{
    "popularity": "88.0000000000",
    "director": "Arun Twari",
    "imdb_score": "8.8000000000",
    "movie_title": "Star Wars",
    "genre": [
        {
            "genre_title": "Action Jackson Arun"
        },
        {
        
            "genre_title": "Adventure"
        },
        {
        
            "genre_title": "Fantasy"
        },
        {
           
            "genre_title": "Sci-Fi"
        }
    ]
}

```

sample response after creation
``` json 
{
    "id": 251,
    "popularity": "88.0000000000",
    "director": "Arun Twari",
    "imdb_score": "8.8000000000",
    "movie_title": "Star Wars",
    "genre": [
        {
            "id": 726,
            "genre_title": "Action Jackson Arun"
        },
        {
            "id": 727,
            "genre_title": "Adventure"
        },
        {
            "id": 728,
            "genre_title": "Fantasy"
        },
        {
            "id": 729,
            "genre_title": "Sci-Fi"
        }
    ]
}

```

4) Update Movies & details (User Authentication required)
```python

https://imdb-task-arun.herokuapp.com/api/251/{PUT}

```
smaple input data for update 
```json
we changed Action Jackson Arun ==> Action Jackson

{
 
    "popularity": "88.0000000000",
    "director": "Arun Twari",
    "imdb_score": "8.8000000000",
    "movie_title": "Star Wars",
    "genre": [
        {
            "id": 726,
            "genre_title": "Action Jackson "
        },
        {
            "id": 727,
            "genre_title": "Adventure"
        },
        {
            "id": 728,
            "genre_title": "Fantasy"
        },
        {
            "id": 729,
            "genre_title": "Sci-Fi"
        }
    ]
}

```
sample output
```json
{
    "id": 251,
    "popularity": "88.0000000000",
    "director": "Arun Twari",
    "imdb_score": "8.8000000000",
    "movie_title": "Star Wars",
    "genre": [
        {
            "id": 726,
            "genre_title": "Action Jackson"
        },
        {
            "id": 727,
            "genre_title": "Adventure"
        },
        {
            "id": 728,
            "genre_title": "Fantasy"
        },
        {
            "id": 729,
            "genre_title": "Sci-Fi"
        }
    ]
}

```
5) Delete record

```python

https://imdb-task-arun.herokuapp.com/api/251/{DELETE}
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)