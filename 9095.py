T = int(input())
result = list(0 for _ in range(11))
result[1]=1
result[2]=2
result[3]=4
out=[]
for j in range(4,11):
    result[j] = result[j-1]+result[j-2]+result[j-3]
for i in range(T):
    n = int(input())
    out.append(result[n])
for i in out:
    print(i)
