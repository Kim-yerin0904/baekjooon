T = int(input())
P =[]
for i in range(T):
    P.append(int(input()))
dp = list(0 for _ in range(101))
dp[1]=1
dp[2]=1
for i in range(3,max(P)+1):
    dp[i] = dp[i-3] + dp[i-2]

for i in P:
    print(dp[i])
