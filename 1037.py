# 1과 본인을 뺀 약수가 순서없이 입력됨
# 약수의 특성인 1,2,4,8 -> 1*8=8 , 2*4=8
# 따라서 입력받은 숫자 중 가장 큰 수 * 가장 작은 수 = 본인

num = int(input())

A = list(map(int, input().split()))

Max = max(A)
Min = min(A)

print(Max*Min)
