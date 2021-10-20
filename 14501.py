N = int(input())
T=[]
P=[]
dp = list(0 for _ in range(N+1))

for i in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)

for j in range(N-1,-1,-1):
        if T[j] > N-j:
            P[j] = 0
            
for i in range(N-1,-1,-1):
    if i+T[i] > N:
        dp[i] = dp[i+1]
        continue
    else:
        dp[i] = max(dp[i+1],P[i]+dp[i+T[i]])

print(dp[0])


