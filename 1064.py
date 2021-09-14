X_a,Y_a,X_b,Y_b,X_c,Y_c = map(int,input().split())

# 한 직선위에 세 점이 있을 때 안됨
# 기울기가 같음
if (Y_b-Y_a) == 0 or (X_b-X_a)== 0:
    inclin_AB = 0
else:
    inclin_AB = (Y_b-Y_a)/(X_b-X_a)

if (Y_c-Y_b) == 0 or (X_c-X_b)== 0:
    inclin_BC = 0
else:
    inclin_BC = (Y_c-Y_b)/(X_c-X_b)
    
if inclin_AB == inclin_BC:
    print(-1.0)

else:
    # AB-BC
    AB=((X_b-X_a)**2+(Y_b-Y_a)**2)**(1/2)
    BC=((X_c-X_b)**2+(Y_c-Y_b)**2)**(1/2)
    AB_BC = 2*AB+2*BC

    # AC-BC
    AC=((X_c-X_a)**2+(Y_c-Y_a)**2)**(1/2)
    BC=((X_c-X_b)**2+(Y_c-Y_b)**2)**(1/2)
    AC_BC = 2*AC+2*BC
        
    # AB-AC
    AB=((X_b-X_a)**2+(Y_b-Y_a)**2)**(1/2)
    AC=((X_c-X_a)**2+(Y_c-Y_a)**2)**(1/2)
    AB_AC = 2*AB+2*AC

    #최대최소 차이
    Max=AB_BC
    if Max < AC_BC:
        Max = AC_BC
    if Max < AB_AC:
        Max = AB_AC

    Min =AB_BC
    if Min > AC_BC:
        Min = AC_BC
    if Min > AB_AC:
        Min = AB_AC

    print(Max-Min)
        

