# S의 최솟값을 구하려면 
# A 원소 최소 * B 원소 최대 이렇게 곱해야함
# 문제에서는 A만 재배열 하는 것이지만 최솟값만 구한다면 이게 빠름
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

result =0 
for i in range(N):
    result += min(A) * max(B)
    A.remove(min(A))
    B.remove(max(B))
print(result)

# 만약 재배열된 A를 구하라고 하면 
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

new_A = list(0 for _ in range(N))
for i in range(N):
    new_A[B.index(max(B))] = min(A)
    B[B.index(max(B))] = -1
    A.remove(min(A))
print(new_A)
