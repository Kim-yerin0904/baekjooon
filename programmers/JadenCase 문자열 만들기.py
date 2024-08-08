def solution(s):
    # 일단 모든 문자를 소문자로 바꾸고 필요한 것만 대문자로 변경하기
    s = s.lower()
    space = False
    
    for i in range(len(s)):
        check = s[i]
        
        # 공백 확인
        if check == " ":
            space = True
        
        # 공백 다음 문자가 나오면 대문자로
        elif space==True and check.isalpha():
            print(check)
            check = check.upper()
            s = s[:i]+check+s[i+1:]
            space = False
            
        # 공백 다음에 숫자가 나올 경우 그대로
        else:
            space = False
    
    # 앞에 공백이 없는 문자 대문자로
    fir = s[0]
    if fir.isalpha():
        fir = fir.upper()
        s = fir+s[1:]
    return s
