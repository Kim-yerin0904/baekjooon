num = int(input())
score=[]

for i in range(num):
    score.append(int(input()))

dp=list(0 for _ in range(301))
dp[0] = score[0]
if num > 1 :
    dp[1] = score[0] + score[1]
if num >2:   
    dp[2] = max(score[1]+score[2],score[0]+score[2])
if num > 3:
    for i in range(3,num):
        dp[i] = max(dp[i-3]+score[i-1]+score[i],dp[i-2]+score[i])

print(dp[num-1])
