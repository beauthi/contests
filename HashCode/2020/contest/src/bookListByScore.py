#/usr/bin/python3

from parser import *;
def orderBookList(indexlib):
    currentLib = libraries[indexlib]
    orderBookMap = {}
    for book in currentLib['books']:
        orderBookMap[book] = getScore(book)
    orderBookMap = {k: v for k, v in sorted(orderBookMap.items(), key =lambda item: item[1], reverse=True)}
    return orderBookMap.keys()

def getScore(book):
    return books_scores[book]