def han(i):
    if i <100:
        return i
    else:
        count = 99
        while i > 99:
            n = i
            first = n % 10
            n = n // 10
            second = n % 10
            third = n // 10
            i = i -1
            T_S = third - second
            S_F = second - first
            if T_S == S_F:
                count = count +1
        return count

i = int(input())
print(han(i))
