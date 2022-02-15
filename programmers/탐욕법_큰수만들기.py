def solution(number, k):
    answer=''
    count = 0
    for i in range(len(number)-k,0,-1):
        max_int = '0'
        for j in range(count,len(number)-i+1):
            if number[j] > max_int:
                max_int = number[j]
                max_idx = j
                if max_int =='9':
                    break
        answer += max_int
        count = max_idx+1   
    return answer
