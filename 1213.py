name = input()
pellin =""
name_dic ={}
for i in name:
    if i not in name_dic:
        name_dic[i] = 1
    else:
        name_dic[i] += 1
value_list = name_dic.values()
key_list = sorted(name_dic.keys())

count =0
for i in value_list:
    if i % 2 == 1:
        count += 1
        
if count > 1:
    print("I'm Sorry Hansoo")
    
elif len(name) < 3:
    if len(name)==1 or name[0] == name[1]:
        print(name)
    else:
        print("I'm Sorry Hansoo")
else:
    for i in key_list:
        if name_dic[i] % 2 == 1:
            if name_dic[i] !=1 :
                odd = i
                name_dic[odd] -= 1
            else:
                odd = i
                key_list.remove(i)
    try:
        for i in key_list:
            if i == odd:
                pellin += odd*(name_dic[i]//2)
            else:
                pellin += i*(name_dic[i]//2)
        rever_pellin = pellin[::-1]
        print(pellin+odd+rever_pellin)
    except:
        for i in key_list:
            pellin += i*(name_dic[i]//2)
        rever_pellin = pellin[::-1]
        print(pellin+rever_pellin)
