N = int(input())
pin_num = list(0 for _ in range(91))
pin_num[1]= 1
for i in range(2,N+1):
    pin_num[i] = pin_num[i-1]+pin_num[i-2]
print(pin_num[N])
