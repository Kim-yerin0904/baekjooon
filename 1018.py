# W로 시작하면 
# (짝수,짝수) - W
# (짝수,홀수) - B
# (홀수,짝수) - B
# (홀수,홀수) - W
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

# B로 시작하면 
# (짝수,짝수) - B
# (짝수,홀수) - W
# (홀수,짝수) - W
# (홀수,홀수) - B
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

#위에 정의된 함수들이 왜 3차원이냐!
#입력을 한줄 단위로 받았기 때문에 arr[0][0]="WBWBWBWBWB" 이런거임
#따라서 내가 입력받은 arr은 N행 1열로 이루어진 행렬임
#그래서 문자 하나씩 보려면 arr[j][0][k] <- 가운데가 0으로 고정

# N,M 입력 받기 
N, M = map(int,input().split())

# arr에 자르기 전의 판 한줄 단위로 입력 받기 
arr = []
for i in range(0,N):
    arr.append(input().split("/n"))

#최솟값 아무거나 저장 나는 제일 처음 0이고, 시작이 W일 때를 저장함 
Min = start_W(arr,0,0)

# 8*8의 크기로 잘라서 사용하기 때문에 index가 N-7,M-7일 때까지 증가
# 최솟값에 저장시켰던 값과 비교하여 더 작은게 나오면 바꾸기
for start_num_N in range(0,N-7):
    for start_num_M in range(0,M-7):
        if Min > start_B(arr,start_num_N,start_num_M):
            Min = start_B(arr,start_num_N,start_num_M)
        if Min > start_W(arr,start_num_N,start_num_M):
            Min = start_W(arr,start_num_N,start_num_M)
print(Min)


