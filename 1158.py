N,K=map(int,input().split())

count=K-1
cycle=list(range(1,N+1))
result=[]
i=2

while len(cycle) != 0:
    if len(cycle) >= count+1:
        result_num = cycle.pop(count)
        result.append(result_num)
        count += (K-1)
        i+=1
    else:
        count = count % len(cycle)
        result_num = cycle.pop(count)
        result.append(result_num)
        i=2
        count += (K-1)
        

result_str = str(result)[1:-1]
print("<",result_str,">",sep='')


