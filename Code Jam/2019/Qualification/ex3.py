t = int(input())
for i in range(t):
    n = list(map(int, input()))[0]
    l = list(map(int, input()))
    primes = [x for x in range(n) if all(n % i for i in xrange(2, n))]
    
