num = int(input())
couple = int(input())
connect=[]
for i in range(couple):
    connect.append(sorted(list(map(int,input().split()))))
connect.sort()
print(connect)
virus={1}
for i in range(couple):
    if connect[i][0] in virus:
        virus.add(connect[i][1])
    elif connect[i][1] in virus:
        virus.add(connect[i][0])

for i in range(couple):
    if connect[i][0] in virus:
        virus.add(connect[i][1])
    elif connect[i][1] in virus:
        virus.add(connect[i][0])

print(virus)
