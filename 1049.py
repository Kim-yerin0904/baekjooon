N,M = map(int,input().split())
set_price =[]
single_price = []

for i in range(M):
    set_pr,single_pr=map(int,input().split())
    set_price.append(set_pr)
    single_price.append(single_pr)

set_need = N // 6
single_need = N % 6

only_set = set_need * min(set_price)
if single_need != 0:
    only_set += min(set_price)
only_single = N * min(single_price)
set_single = set_need * min(set_price) + single_need *min(single_price)

print(min(only_set,only_single,set_single))
