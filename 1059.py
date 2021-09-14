#좋은 구간

L = int(input())
S = list(map(int,input().split()))

#S집합 오름차순 정렬
S.sort()

n = int(input())

count =0

# test case가 n이 S사이에 있는 것만 나왔지만 
# 조건을 보면 좋은 구간인 A<= x <= B 를 만족하는 모든 정수 x가 
# 집합 S에 속하지 않는다고 했고 n은 1과 같거나 크고 집합S에서 가장 큰 정수와 같거나 작기 때문에
# n이 S집합의 최소보다 작을 때와 S집합에 포함될 때를 고려

#n이 S집합의 최소보다 작을 때  
#좋은구간은 [1:n ~ n:S[0]-1]
if n < S[0]:
    Min = 1     #최소는 무조건 1 ->A와 B는 양의 정수이므로
    Max = S[0]-1
    while Min < n:  #A가 n보다 작을 때
        for j in range(n,Max+1):
            count += 1
        Min += 1
    if Min == n:    #A=n일 때
        for k in range(n+1,Max+1):
            count+=1

#n이 S집합의 사이에 있을 때, S집합 원소랑 같을 때
else:
    # n이 S집합의 몇번째 원소 사이에 있는지 알아보고
    # A의 최소와 B의 최대 정하기
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
     
    #n이 S집합의 원소와 같으면 조건에 해당되는게 없어서 바로 프린트

print(count)
                
