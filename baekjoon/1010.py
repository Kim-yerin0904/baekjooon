#순서가 있는 순열 mCn = m!/n!(m-n)!
num = int(input())
result=[]

for i in range(0,num):
    N, M = map(int,input().split())
    if M-N == 0:
        result.append(1)
    else:
        last = 1
        for j in range(N+1, M+1):
            last = last * j
        for k in range(1,M-N+1):
            last = last // k
            #/=는 나누기를 float로 연산하기 때문에 오차가 발생
            #//=는 나누기를 int로 나타냄
        result.append(last)

for r in result:
    print(r)
