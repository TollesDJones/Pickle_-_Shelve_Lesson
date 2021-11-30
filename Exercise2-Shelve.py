# Use shelve to store persistent Favorites lists
# Nested Dictionaries

import  shelve
from imdb import IMDb

# Create an IMDB object
# ia = IMDb()
# results = ia.search_movie('Jaws')
# print(results)

s = shelve.open('media.db')

Movies = {1: {'Name': 'Jurassic Park', 'Date': '1993', 'Rating': '8.1'},
          2: {'Name': 'National Lampoons Christmas Vacation', 'Date': '1989', 'Rating': '7.6'},
          3: {'Name': 'Jaws', 'Date': '1975', 'Rating': '8.0'}
          }

games = {1: {'Title': 'Red Dead Redemption II', 'Date': '2018', 'ESRB': 'M'},
         2: {'Title': 'GTAV', 'Date': '2013', 'ESRB': 'M'}
         }

# def add_item(item_id, item_type):
#     # Keys
#     title =
#     date
#     ESRB
#
#     item_type[item_id: ]
#     # Value

try:
    s['movie_shelf'] = Movies
    s['game_shelf'] = games
finally:
    s.close()




# open the shelved items

try:
    s = shelve.open('media.db')
    # existing = s['movie_shelf']
except RuntimeError:
    print('Error')

current_keys = list(s.keys())
print(current_keys)

for i in s:
    print(i + '\n', str(s[i]) + '\n')

print('\n'*3)
print(s['movie_shelf'])
movies = s['movie_shelf']
print(movies)
for i in movies:
    print(movies[i])
