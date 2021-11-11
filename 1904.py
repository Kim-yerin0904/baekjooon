import sys
N = int(sys.stdin.readline())


dp=[1,2]
for i in range(2,N):
    dp.append((dp[i-1]+dp[i-2])%15746)

print(dp[N-1])


'''
dp = list(0 for _ in range(N))
dp[0]=1
dp[1]=2

def dp_func(n):
    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = dp_func(n-2) + dp_func(n-1)
        return dp[n]

print(dp_func(N-1)%15746)
'''
