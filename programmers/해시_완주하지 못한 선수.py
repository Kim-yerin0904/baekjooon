def solution(participant, completion): 
    participant.sort()
    completion.sort()
    j=0
    for i in range(j,len(completion)): 
        if(participant[i] != completion[i]): 
            return participant[i] 
        j+=1
    return participant[-1]
