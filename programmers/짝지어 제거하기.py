def solution(s):
    answer = 0
    stack =[]

    for i in s:
        if stack == []:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
                
    if stack == []:
        return 1
    return answer
