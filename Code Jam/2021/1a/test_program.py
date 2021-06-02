def function(param):
    for i in range(0, 10000):
        print(param + i)
    a = 0
    while a != 5:
        a = i % 8
        i -= 1
    bite()

def bite():
    for i in range(10000):
        print("bite")


function(123)
