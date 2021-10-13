N = int(input())

result = list(False for _ in range(1000002))
result[1] = 0

for i in range(2,N+1):
    if i % 6 == 0:
        result[i] = min(result[i-1]+1,result[i//3] +1,result[i//2] +1)
    elif i % 3 == 0:
        result[i] = min(result[i-1]+1,result[i//3] +1)   
    elif i % 2 == 0:
        result[i] = min(result[i//2] +1,result[i-1] +1)

    if i % 3 != 0 and i % 2 != 0:
        result[i] = result[i-1] +1

print(result[N])
