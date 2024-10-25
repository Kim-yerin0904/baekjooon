def solution(n):
    ans = 1
    if n == 1:
        return ans
    
    while n != 2:
        if n % 2 == 0:
            n //= 2
            continue
        else:
            ans += 1
            n -= 1

    return ans
