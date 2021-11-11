import sys
stick = list(sys.stdin.readline().rstrip())
open_list=0
sum = 0
i=0
while i < (len(stick)-1):
    if stick[i] =="(" and stick[i+1]==")":
        i += 1
        sum += open_list
    elif stick[i] =="(":
        open_list+=1
    elif stick[i] ==")":
        open_list -=1
        sum += 1
    i += 1
    
if stick[len(stick)-1]  ==")":
    open_list -=1
    sum += 1

print(sum)
