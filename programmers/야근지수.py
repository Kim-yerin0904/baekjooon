def solution(n, works):
    answer = 0
    works_sort = sorted(works,reverse=True)
    max_num = works_sort[0]
    while sum(works_sort) > 0 and n != 0:
        for i in range(len(works_sort)):
            if max_num == works_sort[i]:
                if n > 0:
                    works_sort[i] -= 1
                    n -= 1
                else:
                    break
            else:
                break
        max_num -= 1
    
    for i in works_sort:
        answer += i**2
        
    return answer
