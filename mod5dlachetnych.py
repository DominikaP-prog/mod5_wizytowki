import random
from datetime import datetime

# Klasa bazowa dla filmów i seriali
class Media:
    def __init__(self, title, release_year, genre, views=0):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.views = views

    def play(self):
        self.views += 1

# Klasa dla filmów
class Movie(Media):
    def __str__(self):
        return f"{self.title} ({self.release_year})"

# Klasa dla seriali
class Series(Media):
    def __init__(self, title, release_year, genre, episode, season, views=0):
        super().__init__(title, release_year, genre, views)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f"{self.title} S{self.season:02d}E{self.episode:02d}"

# Funkcja do pobierania wszystkich filmów z biblioteki
def get_movies(library):
    return sorted([item for item in library if isinstance(item, Movie)], key=lambda x: x.title)

# Funkcja do pobierania wszystkich seriali z biblioteki
def get_series(library):
    return sorted([item for item in library if isinstance(item, Series)], key=lambda x: x.title)

# Funkcja do wyszukiwania filmu lub serialu po tytule
def search(library, title):
    for item in library:
        if item.title.lower() == title.lower():
            return item
    return None

# Funkcja do generowania losowych odtworzeń dla losowego elementu z biblioteki
def generate_views(library):
    item = random.choice(library)
    item.views += random.randint(1, 100)

# Funkcja do uruchomienia generate_views 10 razy
def run_generate_views(library):
    for _ in range(10):
        generate_views(library)

# Funkcja do pobierania najpopularniejszych tytułów
def top_titles(library, n, content_type=None):
    if content_type == 'movie':
        items = get_movies(library)
    elif content_type == 'series':
        items = get_series(library)
    else:
        items = library

    return sorted(items, key=lambda x: x.views, reverse=True)[:n]

# Funkcja do dodawania pełnych sezonów seriali do biblioteki
def add_full_season(library, title, release_year, genre, season_number, episodes_count):
    for episode in range(1, episodes_count + 1):
        library.append(Series(title, release_year, genre, episode, season_number))

# Funkcja zewnętrzna do wyświetlania liczby odcinków danego serialu dostępnych w bibliotece
def count_episodes(library, title):
    return len([item for item in library if isinstance(item, Series) and item.title == title])

# Przykład użycia
print("Biblioteka filmów")

library = [
    Movie("Pulp Fiction", 1994, "Crime"),
    Movie("The Godfather", 1972, "Crime"),
]

add_full_season(library, "The Simpsons", 1989, "Animation", 1, 13)
add_full_season(library, "Breaking Bad", 2008, "Drama", 1, 7)

run_generate_views(library)

print("\nNajpopularniejsze filmy i seriale dnia", datetime.now().strftime("%d.%m.%Y"))

for title in top_titles(library, 3):
    print(f"{title} - {title.views} odtworzeń")

print("\nLiczba odcinków The Simpsons:", count_episodes(library, "The Simpsons"))
print("Liczba odcinków Breaking Bad:", count_episodes(library, "Breaking Bad"))
