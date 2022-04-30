from random import randint
from datetime import date

class Movie:
    def __init__(self, title, date, genre):
        self.title = title
        self.date = date
        self.genre = genre
        self.nu_of_plays = 0

    def play(self):
        self.nu_of_plays = self.nu_of_plays + 1
        return f'Odtworzono {self.nu_of_plays} razy'

    def __str__(self):
        return f'{self.title} ({self.date})'

class Series(Movie):
    def __init__(self, episode, season, *args):
        super().__init__(*args)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'{self.title} S{self.season.zfill(2)}E{self.episode.zfill(2)}'


movies_list = [
        Movie('Pulp Fiction', '1994', 'Action'),
        Series('3', '3', '4400', '2007', 'Sci-Fi'),
        Movie('Apocalypse Now!', '1978', 'War'),
        Series('12', '2', 'Dexter', '2012', 'Criminal'),
        Movie('Taxi Driver', '1975', 'Drama'),
        Series('1', '1', 'Dr. House', '2005', 'Medical Drama'),
        Movie('Inglorious Basterds', '2009', 'Drama'),
        Series('7', '6', 'Futurama', '2002', 'Cartoon'),
        Movie('Fulp Piction', '1997', 'Drama'),
        Series('6', '9', 'Family Guy', '1994', 'Cartoon'),
    ]

def get_movies(list):
    movies = []
    for item in list:
        if type(item) == Movie:
            movies.append(item)
    movies.sort(key = lambda item: item.title)
    return movies

def get_series(list):
    series = []
    for item in list:
        if type(item) == Series:
            series.append(item)
    series.sort(key = lambda item: item.title)
    return series

def search(title, list):
    for item in list:
        if item.title == title:
            return item

    return None

def generate_views(list):
    movie = list[randint(0, len(list) - 1)]
    movie.nu_of_plays = movie.nu_of_plays + randint(1, 100)
    return movie

def run_generate_views(list):
    for i in range(10):
        item = generate_views(list)
        
def top_titles(list, count):
    list.sort(key = lambda item: item.nu_of_plays, reverse=True)
    return list[:count]

print('Biblioteka filmów')
run_generate_views(movies_list)

today = date.today().strftime("%d.%m.%Y")
print(f'Najpopularniejsze filmy i seriale dnia {today}')
    
for item in top_titles(movies_list, 3):
    print(f'{item} wyświetlone {item.nu_of_plays} razy')

#for item in get_movies(movies_list):
#    print(item)

#for item in get_series(movies_list):
#    print(item)

#print(search('4400', movies_list))