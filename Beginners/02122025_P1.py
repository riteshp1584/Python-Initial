list_1 = [[1,2,3],
          [4,5,6],
          [7,8,9]]

col_2 = [row[1] for row in list_1]

print(col_2)



my_numbers = [10, 8, 3, 22, 33, 7, 11, 100, 54]

my_numbers.sort()

print(my_numbers)

pl = ["Python", "Swift", "Java", 'C++', "Go", "Rust"]

pl.sort()

print(pl)

pl.sort(key=len)

print(pl)




programming_languages = [
    {'language': 'Python', 'year': 1991},
    {'language': 'Swift',  'year': 2014},
    {'language': 'Java',   'year': 1995},
    {'language': 'C++',    'year': 1985},
    {'language': 'Go',     'year': 2007},
    {'language': 'Rust',   'year': 2010},
]

def get_year(element):
    return element['year']

programming_languages.sort(key=get_year)

print(programming_languages)
