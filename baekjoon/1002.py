# 두 원이 접하는 곳이 재명의 위치
# 두 원이 접할 수 있는 경우의 수를 생각!

T = int(input())
result=[]

for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    distance12 = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    
    r=(r1+r2)

    # 중점이 같을 때
    if distance12 == 0:
        # 반지름도 같으면 똑같은 원 2개니까 무한대
        if r1 == r2:
            result.append(-1)
        # 반지름이 다르면 절대 만날 수 없음
        else:
            result.append(0)
    # 중점 거리가 반지름 더한 것보다 크면 두 원은 만날 수 없음        
    elif distance12 > r:
        result.append(0)
    
    # 한 원이 다른 원을 부분이나 완전히 포함 할때 
    elif distance12 < r:
        # 중점거리와 작은 원의 반지름을 더했을 때 큰원의 반지름보다 작으면
        # 큰원이 작은 원을 완전히 포함하고 접점은 없음
        if distance12+min(r1,r2) < max(r1,r2):
            result.append(0)
        # 중점거리에 작은원 반지름을 더해서 큰원의 반지름과 같으면
        # 원은 완전히 포함된 채로 한 부분이 맞닿아 있음 
        elif distance12+min(r1,r2) == max(r1,r2):
            result.append(1)
        # 그외는 다 2개 포함
        else:
            result.append(2)
    # 중점 거리와 반지름 더한 값이 같으면 두원은 포함되지 않은 채로 한점을 맞닿아 있음
    else:
        result.append(1)

for j in result:
    print(j)
        
