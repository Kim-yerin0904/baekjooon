result = 0

#2
def move_left(lis):
    global result
    a = lis.pop(0)
    lis.append(a)
    result += 1
#3
def move_right(lis):
    global result
    a = lis.pop(-1)
    lis.insert(0,a)
    result += 1

N,M= map(int,input().split())
want = list(map(int,input().split()))
A = list(i for i in range(1,N+1))

while len(want) != 0:
    if want[0] == A[0]:
        del A[0]
        del want[0]

    elif A.index(want[0]) > len(A) // 2:
        while want[0] != A[0]:
            move_right(A)
        
    else:
        while want[0] != A[0]:
            move_left(A)
            
print(result)

        
    
