import sys
N,M = map(int,sys.stdin.readline().split())

s = []

def dfs(start):
    if len(s)==M:
        print(*s,sep=' ')
        return
    if s:
        for i in range(s[-1],N+1):
            s.append(i)
            dfs(i+1)
            s.pop()
    else:
        for i in range(1,N+1):
            s.append(i)
            dfs(i+1)
            s.pop()

dfs(1)
