def solution(s):
    leng = len(s)
    answer = [0,0]
    
    while s != '1':
        c = 0
        for i in s:
            if i == '1':
                c += 1
        answer[1] += (leng - c)

        s=''
        while c > 0:
            s += str(c%2)
            c //= 2
        answer[0] += 1
        s = s[::-1]
        leng = len(s)

    return answer
