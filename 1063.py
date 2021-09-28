# 체스판을 그냥 2차원 배열로 만들어서 입력받은 값을 2차원 배열에 맞게 고쳐서 계산
# 각 움직임마다 행과 렬이 어떻게 변하는지 
# R=(0,+1) L=(0,-1) B=(+1,0) T=(-1,0) RT=(-1,+1) LT=(-1,-1) RB=(+1,+1) LB=(+1,-1)
# try&except문을 활용하여 try에서 말이 체스판 밖으로 나가 range에서 벗어나는 에러 발생시 except로 넘어감
# 하지만, 리스트에서 음수는 뒤에서 세는 거로 range에서 벗어나는게 아니라서 따로 if문 만들어줌
# try&except문은 에러가 나면 실행을 중단하고 except로 가는 거여서 행과 열을 바꾸기 전에 에러 체크용 넣어주기
# 킹과 돌이 만날 때만 둘이 이동하고 둘 중 하나라도 리스트에서 벗어나면 동작 무시, 만나지 않으면 킹만 움직임
# 결과 출력도 리스트에서 체스판만의 배열로 변경 후 
chess=[]

def R(K_a,K_b,S_a,S_b):
    global chess
    try:
        if chess[K_a][K_b+1] == "Stone":    
            chess[K_a][K_b+1]
            chess[S_a][S_b+1]
            K_b+=1  
            S_b +=1
            chess[S_a][S_b] ="Stone"
            chess[K_a][K_b] = "King"
            chess[K_a][K_b-1] =False
            chess[S_a][S_b-1] = False
        else:
            chess[K_a][K_b+1]
            K_b += 1 
            chess[K_a][K_b] = "King"
            chess[K_a][K_b-1] = False
        return(K_a,K_b,S_a,S_b)
    except:
        return(K_a,K_b,S_a,S_b)

def L(K_a,K_b,S_a,S_b):
    try:
        if chess[K_a][K_b-1] == "Stone":    
            chess[K_a][K_b-1]
            chess[S_a][S_b-1]
            if K_b-1 >= 0 and S_b-1 >= 0:
                K_b-=1 
                S_b -=1
                chess[S_a][S_b] ="Stone"
                chess[K_a][K_b] = "King"
                chess[S_a][S_b+1] = False
                chess[K_a][K_b+1] = False   
            else:
                chess[K_a][K_b] = "King"
        else:
            chess[K_a][K_b-1]
            if K_b-1 >= 0:
                K_b -= 1 
                chess[K_a][K_b] = "King"
                chess[K_a][K_b+1] = False
        return(K_a,K_b,S_a,S_b)
    except:
        return(K_a,K_b,S_a,S_b)

def B(K_a,K_b,S_a,S_b):
    try:
        if chess[K_a+1][K_b] == "Stone": 
            chess[K_a+1][K_b]
            chess[S_a+1][S_b]
            K_a+=1
            S_a +=1
            chess[S_a][S_b] ="Stone"
            chess[K_a][K_b] = "King"
            chess[K_a-1][K_b] = False
            chess[S_a-1][S_b] = False
        else:
            chess[K_a+1][K_b]
            K_a += 1
            chess[K_a][K_b] = "King"
            chess[K_a-1][K_b] = False
        return(K_a,K_b,S_a,S_b)
    except:
        return(K_a,K_b,S_a,S_b)


def T(K_a,K_b,S_a,S_b):
    try:
        if chess[K_a-1][K_b] == "Stone":
            chess[K_a-1][K_b]
            chess[S_a-1][S_b]
            if K_a-1 >= 0 and S_a-1 >= 0:
                K_a-=1
                S_a -=1
                chess[S_a][S_b] ="Stone"
                chess[K_a][K_b] = "King"
                chess[K_a+1][K_b]=False
                chess[S_a+1][S_b] = False
        else:
            chess[K_a-1][K_b]
            if K_a-1 >= 0:
                K_a-=1
                chess[K_a][K_b] = "King"
                chess[K_a+1][K_b]=False
            
        return(K_a,K_b,S_a,S_b)
    except:
        return(K_a,K_b,S_a,S_b)

def RT(K_a,K_b,S_a,S_b):
    try:
        if chess[K_a-1][K_b+1] == "Stone":
            chess[K_a-1][K_b+1]
            chess[S_a-1][S_b+1]
            if K_a-1 >= 0 and S_a-1 >= 0:
                K_a-=1
                K_b+=1
                S_b +=1
                S_a -= 1
                chess[S_a][S_b] ="Stone"
                chess[K_a][K_b] = "King"
                chess[K_a+1][K_b-1]=False
                chess[S_a+1][S_b-1] = False
        else:
             chess[K_a-1][K_b+1]
            if K_a-1 >= 0:
                K_a-=1
                K_b+=1
                chess[K_a][K_b] = "King"
                chess[K_a+1][K_b-1]=False
        return(K_a,K_b,S_a,S_b)
    except:
        return(K_a,K_b,S_a,S_b)

def LT(K_a,K_b,S_a,S_b):
    try:
        if chess[K_a-1][K_b-1] == "Stone":
            chess[K_a-1][K_b-1]
            chess[S_a-1][S_b-1]
            if K_a-1 >= 0 and K_b-1 >= 0 and S_a-1 >= 0 and S_b-1 >= 0:
                K_b-=1
                K_a-=1
                S_b -=1
                S_a -= 1
                chess[S_a][S_b] ="Stone"
                chess[K_a][K_b] = "King"
                chess[K_a+1][K_b+1]=False
                chess[S_a+1][S_b+1] = False
        else:
            chess[K_a-1][K_b-1]
            if K_a-1 >= 0 and K_b-1 >= 0:
                K_b-=1
                K_a-=1
                chess[K_a][K_b] = "King"
                chess[K_a+1][K_b+1]=False
        return(K_a,K_b,S_a,S_b)
    except:
        return(K_a,K_b,S_a,S_b)

def RB(K_a,K_b,S_a,S_b):
    try:
        if chess[K_a+1][K_b+1] == "Stone":
            chess[K_a+1][K_b+1]
            chess[S_a+1][S_b+1]
            K_b+=1
            K_a+=1
            S_b +=1
            S_a += 1
            chess[S_a][S_b] ="Stone"
            chess[K_a][K_b] = "King"
            chess[K_a-1][K_b-1]=False
            chess[S_a-1][S_b-1] = False
        else:
            chess[K_a+1][K_b+1]
            K_b+=1
            K_a+=1
            chess[K_a][K_b] = "King"
            chess[K_a-1][K_b-1]=False
        return(K_a,K_b,S_a,S_b)
    except:
        return(K_a,K_b,S_a,S_b)

def LB(K_a,K_b,S_a,S_b):
    try:
        if chess[K_a+1][K_b-1] == "Stone":
            chess[K_a+1][K_b-1]
            chess[S_a+1][S_b-1]
            if K_b-1 >= 0 and S_b-1 >= 0:
                K_b-=1
                K_a+=1
                S_b -=1
                S_a += 1
                chess[S_a][S_b] ="Stone"
                chess[K_a][K_b] = "King"
                chess[K_a-1][K_b+1]=False
                chess[S_a-1][S_b+1] = False
        else:
            chess[K_a+1][K_b-1]
            if K_b-1 >= 0:
                K_b-=1
                K_a+=1
                chess[K_a][K_b] = "King"
                chess[K_a-1][K_b+1]=False
        return(K_a,K_b,S_a,S_b)
    except:
        return(K_a,K_b,S_a,S_b)
    
# 입력이 문자와 숫자 혼합이어서 문자로 받고 count만 숫자로 고치기
K,S,count = input().split()
count = int(count)

# 체스판 배열에 쓰이는 알파벳 1행-A,2행-B ...
alphabet = ["A","B","C","D","E","F","G","H"]

# 모두 False로 체스판 초기값 설정
chess=[]
for _ in range(8):
    chess.append(list(False for _ in range(8)))

# 만약 A1이라면 문자가 행 숫자가 열이므로 리스트와 반대 (7,0)
# 그러므로 체스판 표기 열은 밑에가 작으니까 8-열
# 행은 위의 알파벳 리스트의 위치

# 킹 위치 표시
chess[8 - int(K[1])][alphabet.index(K[0])] = "King"
K_a = 8 - int(K[1])
K_b = alphabet.index(K[0])

# 돌 위치 표시
chess[8 -int(S[1])][alphabet.index(S[0])] = "Stone"
S_a = 8 -int(S[1])
S_b = alphabet.index(S[0])

for i in range(count):
    move = input()
    if move == "R":
        K_a,K_b,S_a,S_b = R(K_a,K_b,S_a,S_b)
    elif move == "L":
        K_a,K_b,S_a,S_b = L(K_a,K_b,S_a,S_b)
    elif move == "B":
        K_a,K_b,S_a,S_b = B(K_a,K_b,S_a,S_b)
    elif move == "T":
        K_a,K_b,S_a,S_b = T(K_a,K_b,S_a,S_b)
    elif move == "RT":
        K_a,K_b,S_a,S_b = RT(K_a,K_b,S_a,S_b)
    elif move == "LT":
        K_a,K_b,S_a,S_b = LT(K_a,K_b,S_a,S_b)
    elif move == "RB":
        K_a,K_b,S_a,S_b = RB(K_a,K_b,S_a,S_b)
    elif move == "LB":
        K_a,K_b,S_a,S_b = LB(K_a,K_b,S_a,S_b)

# 다시 체스판 표기 바꾸기
# 옮긴 후 king 위치
result_K_1 = 8 - K_a
result_K_0 = alphabet[K_b]

# 옮긴 후 돌 위치
result_S_1 = 8-S_a
result_S_0 = alphabet[S_b]

print(result_K_0,result_K_1,sep="")
print(result_S_0,result_S_1,sep="")
