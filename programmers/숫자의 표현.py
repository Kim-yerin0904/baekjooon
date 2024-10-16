def solution(n):
    # 연속된 숫자합
    sum = 0
    # n은 자기 자신도 답이므로 1에서 시작
    answer = 1
    # i는 연속하는 첫 숫자
    for i in range(1,n):
        # 고로 i부터 n까지 i+(i+1)+(i+2)+...이렇게 더하다가
        for j in range (i,n):
            sum += j
            # sum이 n과 같아지면 answer에 +1
            if sum == n:
                answer += 1
            # sum이 n보다 커지면 sum 초기화 후 연속하는 첫 숫자+1 하고 다시 반복
            elif sum > n:
                sum = 0
                break
            
    return answer
