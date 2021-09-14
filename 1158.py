#1234567에서 3,6,2,7,5,4,1 순서면
#index가 K-1씩 커진 것을 알 수 있음

N,K=map(int,input().split())

#index용이어서 -1함
count=K-1

#1~N번까지의 사람들 리스트로 만들기
cycle=list(range(1,N+1))

result=[]

#cycle 리스트에 있는 사람이 모두 없을 때까지 반복
while len(cycle) != 0:
    #cycle의 사람 수가 index보다 많으면 그냥 뺄수 있음
    if len(cycle) >= count+1:
        result_num = cycle.pop(count)
        result.append(result_num)
        count += (K-1)
    
    #cycle의 사람 수가 index보다 적으면 범위에서 벗어나므로 사람수로 나눠서 나머지를 구함
    else:
        count = count % len(cycle)
        result_num = cycle.pop(count)
        result.append(result_num)
        count += (K-1)     

# 대괄호 없애려고 한거
result_str = str(result)[1:-1]
print("<",result_str,">",sep='')


