N = int(input())
num_list =[]
for _ in range(N):
    num_list.append(int(input()))
num_list.sort()

min_count = 4

for j in num_list:
    try:
        for i in range(0,5):
            if j-(4-i) > 0:
                check = list(i for i in range(j-(4-i),j+1+i))
                count = len(check)
                for k in check:
                    if k in num_list:
                        count -= 1
                if min_count > count:
                    min_count = count
    except:
        continue
            
print(min_count)

