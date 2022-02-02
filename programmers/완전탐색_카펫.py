def solution(brown, yellow):
    answer = []
    ysize =[]
    for i in range(1,int(yellow**(1/2))+1):
        if yellow % i==0:
            ysize.append([i,yellow//i])
    for i in ysize:
        if brown == i[0]*2 + (i[1]+2)*2 :
            answer.append(i[1]+2)
            answer.append(i[0]+2)
    
    return answer
