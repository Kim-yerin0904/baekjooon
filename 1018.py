def start_W(n,start_num_N,start_num_M):    
    error = 0
    for j in range(start_num_N,start_num_N+8):
        for k in range(start_num_M,start_num_M+8):
            if j % 2 == 0:
                if k %2 == 0:
                    #(짝수,짝수)
                    if n[j][0][k] == "B":
                        error += 1
                else:
                    #(짝수,홀수)
                    if n[j][0][k] == "W":
                        error += 1
            else:
                if k % 2 == 1:
                    #(홀수,홀수)
                    if n[j][0][k] == "B":
                        error += 1
                else:
                    #(홀수,짝수)
                    if n[j][0][k] == "W":
                        error += 1
    return(error)

def start_B(n,start_num_N,start_num_M):
    error = 0
    for j in range(start_num_N,start_num_N+8):
        for k in range(start_num_M,start_num_M+8):
            if j % 2 == 0:
                if k %2 == 0:
                    #(짝수,짝수)
                    if n[j][0][k] == "W":
                        error += 1
                else:
                    #(짝수,홀수)
                    if n[j][0][k] == "B":
                        error += 1
            else:
                if k % 2 == 1:
                    #(홀수,홀수)
                    if n[j][0][k] == "W":
                        error += 1
                else:
                    #(홀수,짝수)
                    if n[j][0][k] == "B":
                        error += 1
    return(error)


N, M = map(int,input().split())

arr = []
for i in range(0,N):
    arr.append(input().split("/n"))

Min = start_W(arr,0,0)

for start_num_N in range(0,N-7):
    for start_num_M in range(0,M-7):
        if Min > start_B(arr,start_num_N,start_num_M):
            Min = start_B(arr,start_num_N,start_num_M)
        if Min > start_W(arr,start_num_N,start_num_M):
            Min = start_W(arr,start_num_N,start_num_M)
print(Min)


