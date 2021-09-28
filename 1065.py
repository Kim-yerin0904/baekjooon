# 각 자리수가 등차수열을 이루면 한수
# 99까지는 1 혹은 2자리수이므로 모두가 등차수열을 이룸
# 조건에서 입력받는 i는 1000보다 작다고 했고, 100부터 한수인지 체크하면 되므로 3자리수만 체크하면 됨
# first,second,third에 각각 일의 자리수, 십의 자리수, 백의 자리수를 넣고 빼서 같은지 확인
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
