import statistics
from parser import *
from bookListByScore import *

def get_intersect_score(library_a, library_b):
    intersection = list(set(library_a['books']) & set(library_b['books']))
    score = 0
    for book in intersection:
        score += books_scores[book]
    return 0-score

def get_most_valuable_books(books):
    most_valuable_books = []
    book_score_for_lib = []
    for book in books:
        book_score_for_lib.append(books_scores[book])
    median = statistics.median(book_score_for_lib)

    for book in books:
        if books_scores[book] >= median :
            most_valuable_books.append(book)
    print(median)
    return most_valuable_books

print(get_most_valuable_books(libraries[0]['books']))
print(get_intersect_score(libraries[0], libraries[1]))
