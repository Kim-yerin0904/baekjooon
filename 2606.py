num = int(input())
couple = int(input())
connect=[]
for i in range(couple):
    connect.append(sorted(list(map(int,input().split()))))

connect.sort()
virus=[1]
for i in range(couple):
    if connect[i][0] in virus:
        if connect[i][1] in virus:
            continue
        else:
            virus.append(connect[i][1])
    elif connect[i][1] in virus:
        if connect[i][0] in virus:
            continue
        else:
            virus.append(connect[i][0])
            
for i in range(couple):
    if connect[i][0] in virus:
        if connect[i][1] in virus:
            continue
        else:
            virus.append(connect[i][1])
    elif connect[i][1] in virus:
        if connect[i][0] in virus:
            continue
        else:
            virus.append(connect[i][0])
            
print(virus)
