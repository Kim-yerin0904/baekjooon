def solution(prices):
    answer = []
    for j in range(len(prices)-2):
        time=0
        for i in range(j+1,len(prices)):
            if prices[i] < prices[j]:
                time+=1
                break
            else:
                time+=1
        answer.append(time)
    return answer+[1,0]
