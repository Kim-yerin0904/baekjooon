def solution(people, limit):
    answer = 0
    total = 0
    left = 0
    right = len(people)-1
    people.sort()
    while left < right:
        if people[right]*2 <= limit:
            answer += len(people[left:right+1])//2
            if len(people[left:right+1])%2==1:
                answer += 1
            return answer
        else:
            # 가장 큰 수 일단 넣기
            total += people[right]
            right -= 1
            # 남은 무게가 가장 작은 무게보단 크면 남은 무게에 넘지 않는 가장 큰 수 찾기
            if (limit-total) >= people[left]:
                left += 1
                answer += 1
                total = 0
            # 남은 무게가 가장 작은 무게보다 작으면 더 태울수 없음 
            else:
                answer += 1
                total = 0
    if left == right:
        return answer+1
    else: 
        return answer
