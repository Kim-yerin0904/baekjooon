import sys
import itertools
N = int(sys.stdin.readline())
hp=[]
for _ in range(N):
    hp.append(list(map(int,sys.stdin.readline().split())))

com = list(itertools.combinations(list(i for i in range(1,N+1)),N//2))
order = list(0 for _ in range(len(com)))
j=0
for i in com:
    a = list(itertools.combinations(i,2))
    for b in a:
        order[j] += (hp[b[0]-1][b[1]-1]+hp[b[1]-1][b[0]-1])
    j+=1
min=100
j= -1
for i in range(len(order)//2):
    minus = abs(order[i] - order[j])
    j -= 1
    if minus < min:
        min = minus
print(min)
