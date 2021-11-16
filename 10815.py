import sys
N = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
search = list(map(int,sys.stdin.readline().split()))
card.sort()

for i in search:
    h = N-1
    l = 0
    while card[l+1] != card[h]:
        
        idx = (h+l)//2
        if card[idx] > i:
            h = idx
        elif card[idx] < i:
            l=idx
        else:
            break
    if i not in card[l:h+1]:
        print(0,end=" ")
    else:
        print(1,end=" ")
