L = int(input())
S = list(map(int,input().split()))

#S집합 오름차순 정렬
S.sort()

n = int(input())

count =0

#n이 S집합의 최소보다 작을 때  
if n < S[0]:
    Min = 1
    Max = S[0]-1
    while Min < n:
        for j in range(n,Max+1):
            count += 1
        Min += 1
    if Min == n:
        for k in range(n+1,Max+1):
            count+=1

#n이 S집합의 사이에 있을 때, S집합 원소랑 같을 때
else:
    for i in range(L-1):
        if S[i] < n & n < S[i+1]:
            Min = S[i]+1
            Max = S[i+1]-1
            while Min < n:
                for j in range(n,Max+1):
                    count += 1
                Min += 1
    
            if Min == n:
                for k in range(n+1,Max+1):
                    count+=1

print(count)
                
