def solution(k, tangerine):
    answer = 1
    total = 0
    tangerine_set = set(tangerine)
    count = {}
    for i in tangerine_set:
        count[i] = 0
    for j in tangerine:
        count[j] += 1
    values = list(count.values())
    values.sort(reverse=True)
    for i in values:
        total += i
        if total < k:
            answer += 1
        else:
            break
    return answer
