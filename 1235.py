N = int(input())
stu_num=[]
for _ in range(N):
    stu_num.append(int(input()))

for i in range(1,len(str(stu_num[0]))+1):
    check=[]
    for j in stu_num:
        check.append(j%(10**i))
    if len(check) == len(set(check)):
        print(i)
        break
    
