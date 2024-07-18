def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    while len(A) != 0:
        answer += A.pop() * B.pop()
    return answer 
