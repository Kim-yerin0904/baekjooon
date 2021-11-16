import sys
N = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
search = list(map(int,sys.stdin.readline().split()))

card_dic = {}
for i in card:
    try:
        card_dic[i] += 1
    except:
        card_dic[i] = 1

for i in search:
    try:
        print(card_dic[i],end=" ")
    except:
        print(0,end=" ")
