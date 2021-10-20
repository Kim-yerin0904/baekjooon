def cut_cal(tree,meter):
    cut = 0
    for i in tree:
        if i - meter > 0:
            cut += (i-meter)
    return cut
            
N,M = map(int,input().split())
tree= list(map(int,input().split()))

meter = max(tree)
meter_range = list(i for i in range(0,max(tree)+1))
cut = cut_cal(tree,meter)

if N == 1:
    meter = tree[0]-M

else:        
    while True:
        if len(meter_range) ==2:
            meter = meter_range[0]
            break
        if cut < M:
            meter -= ((meter - meter_range[0]+1) // 2)
            cut = cut_cal(tree,meter)
            if cut > M:
                meter_range=meter_range[meter_range.index(meter):]
            elif cut < M:
                meter_range=meter_range[:meter_range.index(meter)+1]
            else:
                break
        elif cut > M:
            meter += ((meter_range[-1]-meter)//2)
            cut = cut_cal(tree,meter)
            if cut > M:
                meter_range=meter_range[meter_range.index(meter):]
            elif cut < M:
                meter_range=meter_range[:meter_range.index(meter)+1]
            else:
                break
        else:
            break
                
print(meter)
