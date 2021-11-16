import sys
N = int(sys.stdin.readline())
num_list=[]
num_dic={}
for i in range(N):
    num = int(sys.stdin.readline())
    if num in num_dic:
        num_dic[num] += 1
    else:
        num_dic[num] =1
    num_list.append(num)
#1번
print(round(sum(num_list)/N))
#2번
num_list.sort()
print(num_list[N//2])
#3번
high = []
num_set = set(num_list)
count = 0
for i in num_set:
    if num_dic[i] > count:
        high = []
        high.append(i)
        count = num_dic[i]
    elif num_dic[i] == count:
        high.append(i)
if len(high) > 1:
    high.sort()
    print(high[1])
else:
    print(*high)
    
#4번
print(max(num_list)-min(num_list))
