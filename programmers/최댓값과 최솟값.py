def solution(s):
    answer = ''
    #s를 리스트로 변환
    s_list = s.split(" ")
    #int 타입으로 변환
    s_list_int = []
    for i in s_list:
        s_list_int.append(int(i))
    #다시 string으로 바꿔서 저장
    answer = answer + str(min(s_list_int)) + " " + str(max(s_list_int))
    return answer
