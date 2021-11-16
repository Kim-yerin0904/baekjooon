import sys
N = int(sys.stdin.readline())
deque=[]
for _ in range(N):
    order = sys.stdin.readline().strip()

    if order.find("push_front") != -1:
        num = int(order.replace("push_front ",""))
        deque.insert(0,num)
        
    elif order.find("push_back") != -1:
        num = int(order.replace("push_back ",""))
        deque.append(num)
    
    elif order =="pop_front":
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    elif order == "pop_back":
        if deque:
            print(deque.pop())
        else:
            print(-1)

    elif order =="size":
        print(len(deque))
        
    elif order == "empty":
        if len(deque)!=0:
            print(0)
        else:
            print(1)
            
    elif order=="front":
        if len(deque)!=0:
            print(deque[0])
        else:
            print(-1)
            
    elif order == "back":
        if len(deque)!=0:
            print(deque[-1])
        else:
            print(-1)
    

