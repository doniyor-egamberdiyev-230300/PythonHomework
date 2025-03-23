import requests
import random

API_KEY = "26691bd853dfeadca4d4283928547c98"
BASE_URL = "https://api.themoviedb.org/3"

# Fetch available genres
genre_url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
response = requests.get(genre_url)

# Debugging: Check status code
if response.status_code != 200:
    print(f"Error: {response.status_code}, {response.text}")
    exit()

genres = response.json().get("genres", [])

# Display available genres
print("Available genres:")
for genre in genres:
    print(f"{genre['id']}: {genre['name']}")

# User input
genre_id = input("\nEnter the genre ID you want recommendations for: ")

# Fetch movies in the selected genre
movies_url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
response = requests.get(movies_url)

# Debugging: Check status code
if response.status_code != 200:
    print(f"Error: {response.status_code}, {response.text}")
    exit()

movies = response.json().get("results", [])

# Pick a random movie
if movies:
    movie = random.choice(movies)
    print("\n🎬 Recommended Movie:")
    print(f"Title: {movie['title']}")
    print(f"Overview: {movie['overview']}")
    print(f"Rating: {movie['vote_average']}/10")
    print(f"Release Date: {movie['release_date']}")
    print(f"More Info: https://www.themoviedb.org/movie/{movie['id']}")
else:
    print("No movies found for this genre.")
