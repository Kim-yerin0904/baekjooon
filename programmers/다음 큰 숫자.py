def solution(n):
    answer = 0
    bin_n = bin(n)[2:]
    bin_big =''
    
    # 1111, 11, 1
    if bin_n.count('1') == len(bin_n):
        need_1 = bin_n.count('1') - 1
        bin_big = '1' + ((len(bin_n)-need_1) * '0') + (need_1 * '1')
        print('case1) ',bin_n, bin_big)
        
    else:
        # 101010, 11001, 100110
        for i in range(len(bin_n)-1,0,-1):
            if bin_n[i] == '1' and bin_n[i-1] == '0':
                bin_big = bin_n[:i-1]+'1'
                leng = len(bin_n) - len(bin_big)
                need_1 = bin_n.count('1') - bin_big.count('1')
                bin_big = bin_big + ((leng-need_1) * '0') + (need_1 * '1') 
                print('case2) ',bin_n, bin_big)
                break
            else:
                continue
        # 10, 1100 이런 애들
        if bin_big == '':
            need_1 = bin_n.count('1') - 1
            bin_big = '1' + ((len(bin_n)-need_1) * '0') + (need_1 * '1')
            print('case3) ',bin_n, bin_big)
    
    # 이진수를 십진수로 바꾸기
    # i = 0
    # for j in bin_big[::-1]:
    #     answer = answer + (int(j) * (2**i))
    #     i += 1
    answer = int('0b'+bin_big,2)
    return answer
