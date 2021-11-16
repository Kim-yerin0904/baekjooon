import sys
N,M = map(int,sys.stdin.readline().split())
circle = list(i for i in range(1,N+1))
M -= 1
result=[]
count = 0
while len(circle) != 0:
    if count+M > len(circle)-1:
        count = (count+M)%len(circle)
    else:
        count += M
    result.append(circle.pop(count))
result_str=str(result)[1:-1]
print ("<"+result_str+">")
    
