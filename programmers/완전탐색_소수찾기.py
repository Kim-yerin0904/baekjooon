import itertools
def enstanes(max_num):
    prime = [True]*(max_num+1)
    if max_num > 1:
        prime[0] = False
        prime[1] = False
    for i in range(2,max_num+1):
        for j in range(i*2,max_num+1,i):
            prime[j] = False
    return prime
def solution(numbers):
    answer = 0
    num_list =[]
    num_list2=[]
    for i in range(1,len(numbers)+1):
        num_list += list(itertools.permutations(numbers,i))
        
    print(num_list)
    for i in num_list:
        a =""
        for j in i:
            a += j
        num_list2.append(int(a))
    max_num = max(num_list2)
    prime = enstanes(max_num)
    for i in set(num_list2):
        if prime[i]:
            answer += 1
    return answer
