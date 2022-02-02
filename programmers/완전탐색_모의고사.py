def length (list_num,answers):
    a = len(answers) // len(list_num)
    if len(answers) % len(list_num):
        a += 1
    list_num = list_num * a
    return list_num

def counting(list_num,answers):
    count = 0
    for i in range(len(answers)):
        if answers[i] == list_num[i]:
            count += 1
    return count
def compare(count):
    answer =[]
    max = count[0]
    answer.append(1)
    for i in range(1,3):
        if max < count[i]:
            max = count[i]
            answer.clear()
            answer.append(i+1)
        elif max == count[i]:
            answer.append(i+1)
    return answer

def solution(answers):
    num1 = [1,2,3,4,5] 
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0] 
    num1 = length(num1,answers)
    num2 = length(num2,answers)
    num3 = length(num3,answers)
    count[0] = counting(num1,answers)
    count[1] = counting(num2,answers)
    count[2] = counting(num3,answers)
    return compare(count)
