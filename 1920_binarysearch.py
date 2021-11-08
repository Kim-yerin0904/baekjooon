import sys
N = int(sys.stdin.readline())
A = sorted(list(map(int,sys.stdin.readline().split())))
M = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
result = list(0 for _ in range(M))

count = 0

for i in num_list:
    bi_search=[0,N-1]
    
    while bi_search[1]-bi_search[0] != 1:
        
        if i < A[(sum(bi_search)//2)]:
            bi_search[1] = (sum(bi_search)//2)
            
        elif i > A[(sum(bi_search)//2)]:
            bi_search[0] = (sum(bi_search)//2)
            
        else:
            result[count] = 1
            break
            
    if A[bi_search[1]] == i or A[bi_search[0]] == i:
        result[count] = 1
    
    count += 1
    

for j in result:
    print(j)
