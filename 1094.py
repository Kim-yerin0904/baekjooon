stick = 64
total = 0
count = 0

X = int(input())

if X == 64:
    print(1)
else:
    while total != X:
        stick /= 2
        if total + stick <= X:
            total += stick
            count += 1
    print(count)

            


