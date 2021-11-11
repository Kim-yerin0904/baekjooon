import sys
K,N = map(int,sys.stdin.readline().split())
length=[0]*K
for i in range(K):
    length[i] = int(sys.stdin.readline())
    
bi_range = [0,max(length)]
meter = sum(bi_range)//2

def cut_cal(meter):
    sum = 0
    for i in length:
        sum += (i // meter)
    return sum

while bi_range[-1]-bi_range[0] != 1:
    if cut_cal(meter) > N:
        bi_range[0] = meter
        meter = sum(bi_range)//2
        
    elif cut_cal(meter) < N:
        bi_range[-1] = meter
        meter = sum(bi_range)//2

    else:
         break 
        

for i in range(bi_range[-1],meter,-1):
    if cut_cal(i) == N:
        meter = i
        break

print(meter)
