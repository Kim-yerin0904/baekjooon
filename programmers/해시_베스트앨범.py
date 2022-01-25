def solution(genres, plays):
    answer = []
    dic ={}
    #장르별 총합 딕셔너리 저장
    for i,j in zip(genres,plays):
        if i in dic:
            dic[i] += j
        else:
            dic[i] = j
    
    #가장 많은 장르부터 2개씩 인덱스 저장하기
    best = sorted(dic.items(), key=lambda x:x[1],reverse=True)
    for best_key, best_value in best:
        music_list= {}
        for i in range(len(genres)):
            if best_key == genres[i]:
                music_list[i] = plays[i]
        
        #장르에 노래가 하나면 그냥 추가
        if len(music_list) == 1:
            answer.append(genres.index(best_key))
        else:
            count =0
            a = sorted(music_list.items(), key=lambda x:x[1],reverse=True)
            for key,value in a:
                answer.append(key)
                count +=1
                if count ==2:
                    break
    return answer
