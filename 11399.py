N = int(input())
Pi = sorted(list(map(int,input().split())))

result = 0

for i in range(0,N):
    result += Pi[i] * (N-i) 

print(result)
