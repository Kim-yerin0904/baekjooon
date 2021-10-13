N = int(input())

book_dic={}
for _ in range(N):
    title = input()
    if title in book_dic:
        book_dic[title] += 1
    else:
        book_dic[title] = 1
book_sort = sorted(book_dic.items(),key = lambda x:x[1],reverse = True)

compare=[]
for i in range(len(book_sort)-1):
    if book_dic[book_sort[i][0]] == book_dic[book_sort[i+1][0]]:
        compare.append(book_sort[i][0])
        compare.append(book_sort[i+1][0])
    else:
        break
if len(compare) == 0:
    print(book_sort[0][0])
else:
    compare.sort()
    print(compare[0])
