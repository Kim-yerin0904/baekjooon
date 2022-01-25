def solution(progresses, speeds):
    answer = []
    day =[]
    for i in range(len(progresses)):
        day.append((100 - progresses[i]) // speeds[i])
        if ((100 - progresses[i]) % speeds[i]) != 0:
            day[i] += 1
    max = day[0]
    count = 1
    for i in day[1:]:    
        if max < i:
            max = i
            answer.append(count)
            count = 1
        else:
            count += 1
    answer.append(count)
    return answer
