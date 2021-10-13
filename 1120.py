A, B = input().split()
len_A = len(A)
len_B = len(B)
i=0
result = []
while i <= len_B - len_A:
   count = 0
   for j in range(0,len_A):
      if A[j] != B[j+i]:
         count += 1
   result.append(count)
   i += 1

print(min(result))
