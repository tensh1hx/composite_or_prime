x = 1
y = 1
dividers = []

while True:
    if y < x:
        y += 1
    p = x / y
    if x % y == 0:
        dividers.append(y)
    if x <= y:
        if dividers == [1, x]:
            print(x, "is a prime number!")
        y = 0
        x += 1
        dividers.clear()