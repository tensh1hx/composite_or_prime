x = 1
y = 1
dividers = []

while True:
    if y <= x**0.5:
        y += 1
    p = x / y
    if x % y == 0:
        dividers.extend([y,p])
    if x**0.5 < y:
        if len(dividers) < 3 or x < 3:
            print(x, "is a prime number!")
        else:
            print(x, "is a composite number!")
        y = 0
        x += 1
        dividers.clear()
