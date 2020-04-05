#/usr/bin/python3

first_line = input().split()
B, L, D = int(first_line[0]), int(first_line[1]), int(first_line[2])
books_scores = list(map(int, input().split()))

libraries = []
for _ in range(L):
    description = list(map(int, input().split()))
    books = list(map(int, input().split()))
    library = {}
    library['number_books'] = description[0]
    library['signup_duration'] = description[1]
    library['shipping_debit'] = description[2]
    library['books'] = books
    libraries.append(library)
"""
 B : nombre de livres
 L : nombre de bibliothèques
 D : temps qu'on a pour scanner
 books_scores : scores des livres (index : ID du livre, valeur : score)
 libraries : liste de library
 [ library, library, library ]
 library est un dictionnaire ressemblant à ça
 library = {
    'number_books' : 3,
    'signup_duration' : 1,
    'shipping_debit' : 2,
    'books' : [9, 8, 7]
 }
 number_books : nombre de livres dans la lib
 signup_duration : durée de signup en jours
 shipping_debit : nombre de livres que la lib peut sortir par jour
 books : liste dont les valeurs correspondent aux ID des books (0 = index dans books_scores)
"""