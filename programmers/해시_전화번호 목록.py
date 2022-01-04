def solution(phone_book):
    phone_book.sort()
    answer = True
    pre = phone_book[0]
    for i in range(1,len(phone_book)):
        compare = phone_book[i][:len(pre)]
        if pre == compare:
            answer = False
            break
        pre = phone_book[i]
        if answer == False:
            break
    return answer
