import sys
N = int(sys.stdin.readline())
fac = 1
for i in range(2,N+1):
    fac *= i
fac = list(str(fac))
fac.reverse()
count = 0
for i in fac:
    if i != "0":
        print(count)
        break
    else:
        count += 1
