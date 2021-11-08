import sys
T = int(sys.stdin.readline())
que = {}
for _ in range(T):
    N,M = map(int,sys.stdin.readline().split())
    imp = list(map(int,sys.stdin.readline().split()))
    for i in range(N):
        que[i]=imp[i]
    
    count = 0
    order = list(i for i in range(N))
    
    while True:
        now_max = max(imp)
        
        if que[M]==now_max and order[0] ==M:
            imp.remove(now_max)
            count += 1
            print(count)
            break
        
        elif que[order[0]] == now_max:
            del que[order[0]]
            imp.remove(now_max)
            del order[0]
            count += 1
            
        else:
            num = order.pop(0)
            order.append(num)
            
            
