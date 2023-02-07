#code by goonzchief
import json
import requests

def get_movie_details(imdb_id):
    #get your api from omdbapi.com and put it down below
    api_key = "YOUR_OMDBAPI_KEY_HERE"
    response = requests.get(f"http://www.omdbapi.com/?i={imdb_id}&apikey={api_key}")
    movie_data = response.json()
    # you can add some details if you want in a same format I did
    title = movie_data.get("Title")
    imdbrate = movie_data.get("imdbRating")
    storyline = movie_data.get("Plot")
    director = movie_data.get("Director")
    year = movie_data.get("Year")
    genre = movie_data.get("Genre")
    stars = movie_data.get("Actors")
    country = movie_data.get("Country")
    language = movie_data.get("Language")
    movie_details = {
        "Title": title,
        "imdbrate": imdbrate,
        "Storyline": storyline,
        "Stars": stars,
	"Director": director,
	"Year":year,
	"Genre":genre,
    "Language":language,
    "Country":country
    
    }
    with open("movie_details.json", "w") as f:
        json.dump(movie_details, f)
    print("Result saved in movie_details.json")

if __name__ == "__main__":
    imdb_id = input("Enter IMDb ID: ")
    get_movie_details(imdb_id)
