def solution(priorities, location):
    answer=0
    ind_list = list(i for i in range(0,len(priorities)))
    
    while True:
        max_pri = max(priorities)
        while max_pri != priorities[0]:
            a = priorities.pop(0)
            priorities.append(a)
            b = ind_list.pop(0)
            ind_list.append(b)
        if max_pri == priorities[0]:
            priorities[0] = 0
            answer += 1
            if location == ind_list[0]:
                break
    return answer
