#같은 것이 있는 순열
# ex) aaabb -> 5!/3!2!
def cal(i,j,k):
    fin = 1
    for a in range(j+1,i+1):
        fin *= a
    for b in range(2,k+1):
        fin //= b
    return fin

n = int(input())

result = 0
two = n // 2
one = n % 2

for i in range(0,n//2+1):
    if two == 0 or one == 0:
        result += 1
    else:
        result += cal(two+one,two,one)
    two -= 1
    one += 2

print(result)
