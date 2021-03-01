

import string
import random

def userhash(s):
        hsh = 0
        for c in s:
            hsh *= 31
            hsh += ord(c)
        return hsh%(2**32)

def revhash(hsh):
    charset = string.ascii_uppercase + string.digits
    COLLISION_BASE = 5
    
    h1lookup = {}
    for _ in range(100000):
        half1 = ''.join(random.choice(charset) for _ in range(COLLISION_BASE))
        half1hash = userhash(half1)
        h1lookup[half1hash] = half1

    while True:
        half2 = ''.join(random.choice(charset) for _ in range(COLLISION_BASE))
        half2hash = (31**COLLISION_BASE * userhash(half2)) % (2**32)
        rem = (hsh - half2hash) % (2**32)
        if rem in h1lookup:
            return half2 + h1lookup[rem]
    
username = input()
hsh = userhash(username)
collision = revhash(hsh)
print(collision)

