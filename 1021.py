# 앞뒤로 뺄수 있는게 아니라 1번인 맨앞에서만 뽑을 수 있음
# 1번 연산은 del를 이용하여 index=0인 맨앞 제거
result = 0
#2
# 맨앞 추출 맨뒤 추가
def move_left(lis):
    global result
    a = lis.pop(0)
    lis.append(a)
    result += 1
#3
# 맨뒤 추출 맨앞 추가
def move_right(lis):
    global result
    a = lis.pop(-1)
    lis.insert(0,a)
    result += 1

N,M= map(int,input().split())
want = list(map(int,input().split()))
A = list(i for i in range(1,N+1))

# 뽑아야하는 수가 없어질 때까지 반복
while len(want) != 0:
    # 만약 뽑아야하는 수가 A리스트 맨앞이라면 1번 연산
    # 뽑고나면 want에서 삭제
    if want[0] == A[0]:
        del A[0]
        del want[0]
    # 찾는 숫자의 위치가 A의 중간보다 뒤에 있을 때
    # 3번 연산이 더 빠름
    elif A.index(want[0]) > len(A) // 2:
        while want[0] != A[0]:
            move_right(A)
    # 찾는 숫자의 위치가 A의 앞쪽이면 
    # 2번 연산이 빠름
    else:
        while want[0] != A[0]:
            move_left(A)
            
print(result)

        
    
