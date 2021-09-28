N = int(input())
A = list(map(int,input().split()))
B = sorted(A)
P=list(0 for _ in range(N))

for i in A:
    indices_A = list(filter(lambda e:A[e]==i,range(N)))
    indices_B = list(filter(lambda e:B[e]==i,range(N)))
    for j in range(len(indices_A)):
        p_index = indices_A[j]
        p_vaule = indices_B[j]
        P[p_index] = p_vaule

P_new = [str(a) for a in P]
print(" ".join(P_new))
