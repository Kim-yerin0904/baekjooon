switch_num = int(input())
switch_state = list(map(int,input().split()))
student_num = int(input())

for _ in range(student_num):
    sex, num = map(int, input().split())
    if sex ==1:
        for i in range(num-1,switch_num,num):
            if switch_state[i] ==0:
                switch_state[i] =1
            else:
                switch_state[i] =0
    else:
        try:
            i =1
            change =[num-1]
            while num-1-i > -1:
                if switch_state[num-1-i] == switch_state[num-1+i]:
                    change.append(num-1-i)
                    change.append(num-1+i)
                    i += 1
                else:
                    break
            for i in change:
                if switch_state[i] ==0:
                    switch_state[i] =1
                else:
                    switch_state[i] =0
        except:
            for i in change:
                if switch_state[i] ==0:
                    switch_state[i] =1
                else:
                    switch_state[i] =0

i=0
while i+20 <= switch_num:
    print(*switch_state[i:i+20],sep=" ")
    i+=20
if switch_num % 20 != 0:
    print(*switch_state[i:],sep=" ")
