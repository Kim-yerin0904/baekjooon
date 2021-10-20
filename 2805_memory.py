def cut_cal(tree,meter):
    cut = 0
    for i in tree:
        if i - meter > 0:
            cut += (i-meter)
    return cut
            
N,M = map(int,input().split())
tree= list(map(int,input().split()))

meter = max(tree)
meter_range = [0,max(tree)]
cut = cut_cal(tree,meter)

if N == 1:
    meter = tree[0]-M

else:
    while True:
        if len(meter_range) ==2 and (meter_range[1]-meter_range[0])==1:
            meter = meter_range[0]
            break
        if cut < M:
            meter -= ((meter - meter_range[0]+1) // 2)
            cut = cut_cal(tree,meter)
            if cut > M:
                meter_range[0] = meter
            elif cut < M:
                meter_range[-1] = meter
            else:
                break
        elif cut > M:
            meter += ((meter_range[-1]-meter)//2)
            cut = cut_cal(tree,meter)
            if cut > M:
                meter_range[0] = meter
            elif cut < M:
                meter_range[-1] = meter
            else:
                break
        else:
            break
        
print(meter)
