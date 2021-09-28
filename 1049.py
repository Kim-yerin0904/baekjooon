# 적어도 N개를 사는 거니까 N개 이상이면 됨
# 경우의 수는 세트만 사는 경우, 단품만, 세트+단품
N,M = map(int,input().split())
set_price =[]
single_price = []

# 세트와 단품의 가격을 각각 리스트에 추가
for i in range(M):
    set_pr,single_pr=map(int,input().split())
    set_price.append(set_pr)
    single_price.append(single_pr)

# 세트가 몇개 필요한지를 위해
set_need = N // 6
single_need = N % 6

# 최소비용을 구하므로 가격은 입력받은 것 중 가장 작은거!
# 세트만 사는 경우 N을 6으로 나누고 나머지가 있으면 한세트 더 사야함
only_set = set_need * min(set_price)
if single_need != 0:
    only_set += min(set_price)
# 단품만 사는 경우는 N개 사면됨
only_single = N * min(single_price)
# 세트+단품이면 N을 6으로 나눈 몫이 세트 수, 나머지가 단품 수
set_single = set_need * min(set_price) + single_need *min(single_price)

# 위의 세가지 경우 중 가장 작은거 출력
print(min(only_set,only_single,set_single))
