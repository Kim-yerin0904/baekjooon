import sys
N = int(sys.stdin.readline())

card = list(i for i in range(1,N+1))
while len(card) > 1:
    new_card =[]
    for i in range(1,len(card),2):
        new_card.append(card[i])
    if len(card)%2==1:
        num = new_card.pop(0)
        new_card.append(num)
    card = new_card
print(*card)
    
