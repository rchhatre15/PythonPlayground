import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

movies = soup.find_all(name="h3", class_="title")
movie_lst = [movie.getText() for movie in movies]
print(movie_lst)

with open("Starting Code - 100 movies to watch start/movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_lst[::-1]:
        file.write(f"{movie}\n")



