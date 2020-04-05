from parser import *
from bookListByScore import orderBookList

def calcBookScorev1(lib):
    return (library['shipping_debit'] * book_score) / library['signup_duration']


def calcBookScorev2(lib):
    return (library['shipping_debit'] * book_score) / library['signup_duration']

results = {
    'libraries' : libraries,
}


for idx, library in enumerate(results['libraries']):
    library['index'] = idx
    book_score = sum(books_scores[i] for i in library['books'])
    library['score'] = calcBookScorev1(library)
    library['books'] = list(orderBookList(idx))
results['libraries'] = sorted(
    results['libraries'],
    key=lambda x : (x['score'], x['books']),
    reverse=True
)

# amelioration books max
signup_days_total = 0
books_seen = []
for idx, library in enumerate(results['libraries']):
    library['books'] = [book for book in library['books'] if book not in books_seen]
    signup_days_total += library['signup_duration']
    books_left = (library['shipping_debit'] * (D - signup_days_total))
    library['books_max_line'] = books_left
    library['books'] = library['books'][:library['books_max_line']]
    books_seen = list(set(books_seen + library['books']))
results['libraries'] = [library for library in results['libraries'] if (library['books_max_line'] > 0 and len(library['books']) > 0)]
# output
print(len(results['libraries']))
for library in results['libraries']:
    print(library['index'], len(library['books']))
    print(" ".join(str(book) for book in library['books']))
