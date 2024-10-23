def solution(arr):
    answer = arr[-1]
    fin = arr[-1]
    flag = True
    
    if arr[0] == 1:
        arr.pop(0)        
    arr.pop()

    while flag:
        for i in arr:
            if answer%i != 0 :
                answer += fin
                break
            elif len(arr)==1 and answer%i == 0:
                flag = False 
                break
            # answer%i == 0
            else:
                arr.pop(0)
                fin = answer
                break
    
    return answer
