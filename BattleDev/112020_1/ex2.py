import math

n, m = tuple(map(int, input().split()))
routes = {}
for _ in range(n):
    passenger, begin, arrival = tuple(input().split())
    if (begin, arrival) not in routes:
        routes[(begin, arrival)] = [passenger]
    else:
        routes[(begin, arrival)].append(passenger)
number_cars = sum(math.ceil(len(routes[route]) / 3) for route in routes)
print(number_cars)
for route in routes:
    for passengers in [routes[route][_:_+3] for _ in range(0, len(routes[route]), 3)]:
        print(" ".join(passengers))
