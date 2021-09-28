# 이해가 잘 안되서 예제를 대입해서 어떤 숫자 a는 P[A.index(a)]=B.index(a)라는 걸 발견
# 근데 중복되는 숫자는 index함수로 위치를 찾을 때 가장 앞에 있는 것만 찾음
# 따라서 리스트에서 어떤 수의 모든 위치를 찾기 위해 filter 함수 사용

N = int(input())
A = list(map(int,input().split()))
B = sorted(A)   # A의 비내림차순
P=list(0 for _ in range(N))

for i in A:
    #indices에 인덱스 저장
    indices_A = list(filter(lambda e:A[e]==i,range(N)))
    indices_B = list(filter(lambda e:B[e]==i,range(N)))
    for j in range(len(indices_A)):
        p_index = indices_A[j]
        p_vaule = indices_B[j]
        P[p_index] = p_vaule

P_new = [str(a) for a in P]
print(" ".join(P_new))
