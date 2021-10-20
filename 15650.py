import re
import itertools

N,M = map(int,input().split())
num_list = list(i for i in range(1,N+1))

result = itertools.combinations(num_list,M)

for i in result:
    print(*i,end=' ')
    print()

