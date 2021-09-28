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
        
K,S,count = input().split()
count = int(count)
    
alphabet = ["A","B","C","D","E","F","G","H"]
chess=[]
for _ in range(8):
    chess.append(list(False for _ in range(8)))

#킹 위치 표시
chess[8 - int(K[1])][alphabet.index(K[0])] = "King"
K_a = 8 - int(K[1])
K_b = alphabet.index(K[0])

#돌 위치 표시
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

#옮긴 후 king 위치
result_K_1 = 8 - K_a
result_K_0 = alphabet[K_b]

#옮긴 후 돌 위치
result_S_1 = 8-S_a
result_S_0 = alphabet[S_b]

print(result_K_0,result_K_1,sep="")
print(result_S_0,result_S_1,sep="")
