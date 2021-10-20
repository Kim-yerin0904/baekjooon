n = int(input())
num_list = list(i for i in range(1,n+1))
fin = []
for i in range(n):
    fin.append(int(input()))
result=[]
stack=[]
i=0
#아래 boolean은 No일때 result를 안뽑으려고 설정
is_possible =True

#fin에서 빼야할 수가 없으면 반복문 중지
while len(fin) != 0:
    #stack에 아무것도 없으면 무조건 push
    #더 이상 stack에 넣을 수가 없을 수 있으니 index range 제한
    if len(stack)==0 and i < n:
        stack.append(num_list[i])
        result.append("+")
        i += 1
    #stack에 가장 마지막 수보다 빼야할 수가 더 작으면 불가능
    if stack[-1] > fin[0]:
        print("NO")
        is_possible = False
        break
    else:
        #stack에 가장 나중에 들어간 수가 fin의 가장 먼저 빼야할 수와 같으면
        #stack에서 pop하고 fin에서 제거
        if stack[-1] == fin[0]:
            result.append("-")
            del stack[-1]
            del fin[0]
        #push
        else:
            stack.append(num_list[i])
            result.append("+")
            i += 1
if is_possible:
    for j in result:
        print(j)
