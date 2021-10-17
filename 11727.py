n = int(input())

two = n // 2
one = n % 2
result = 1

while two > 0:
    calcu =1
    for i in range(two+one,max(two,one),-1):
        calcu *= i
    for i in range(1,min(two,one)+1):
        calcu //= i
    calcu *= 2**two
    result += calcu
    two -= 1
    one += 2

print(result%10007)
