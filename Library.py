import requests

authors = requests.get('https://www.wolnelektury.pl/api/authors/')

for author in authors.json():
    print(authors["name"])

# genres = requests.get("https://www.wolnelektury.pl/api/books")
# for genre in genres.json():
# print(genre["genres"])


# ma zwrocic kolekcje autorow po imionach, pobrac wszystkie ksiazki, zrobic slownik - jaki autor i jakie ma gatunki - napisane w funkcjach z return\n


names = authors.json()

# print(names)
