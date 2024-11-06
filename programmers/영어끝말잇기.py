def solution(n, words):
    answer = []
    front = words[0][-1]
    # 앞의 문자와 다를 경우
    for i in range(1,len(words)):
        if words[i][0] != front:
            answer.append(i)
            break
        else:
            front = words[i][-1]
    # 중복 단어가 있는 경우
    same = []
    for i in range(len(words)):
        if words.count(words[i]) != 1 and words[i] in same:
            answer.append(i)
            break
        elif words.count(words[i]) != 1:
            same.append(words[i])
    
    # answer가 있다면 탈락한 사람이 있음
    if answer:
        if (min(answer)+1)%n == 0:
            return [n,(min(answer)+1)//n]
        else:
            return [(min(answer)+1)%n,((min(answer)+1)//n)+1]
    # answer가 없으면 탈락한 사람 없음
    else: 
        return [0,0]
