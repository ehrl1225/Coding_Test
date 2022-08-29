def decimal_to_ternary(decimal_n):
    num = decimal_n
    result = ""
    while(num//3>0):
        result = str(num%3)+result
        num = num//3
    result = str(num % 3) + result
    return result

def ternary_to_decimal(ternary_s):
    result = 0
    for index, i in enumerate(ternary_s[::-1]):
        if index==0:
            result+=int(i)
        else:
            result+=(3**index)*int(i)
    return result

def solution(n):
    ternary_s = decimal_to_ternary(n)[::-1]
    answer = ternary_to_decimal(ternary_s)
    return answer

if __name__ == '__main__':
    print(ternary_to_decimal("22111"))