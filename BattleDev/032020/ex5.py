from itertools import combinations

def is_palindrome(word):
    if word == '':
        return False
    i = 0
    word_length = len(word)
    while i < (word_length / 2):
        if word[i] != word[word_length - i - 1]:
            return False
        i += 1
    return True

def get_palindromes(word, n):
    if k == 1:
        if not is_palindrome(word):
            return -1
        else:
            return word
    indexes_possibilities = combinations(range(len(word)), n)
    for indexes in indexes_possibilities:
        words = [word[i:j] for i, j in zip((0,) + indexes, indexes + (None,))]
        if all(is_palindrome(word) for word in words):
            return words
    return -1

_, k = tuple(map(int, input().split()))
brochette = input()
palindromes = get_palindromes(brochette, k - 1)
if palindromes == -1:
    print("IMPOSSIBLE")
else:
    print(" ".join(palindrome for palindrome in palindromes))
