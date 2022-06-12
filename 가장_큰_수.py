def max_num(numbers):
    max_number = numbers[0]
    for i in numbers[1:]:
        len_min = min(len(str(i)),len(str(max_number)))
        for j in range(len_min):
            if str(max_number)[j]<str(i)[j]:
                max_number=i
            elif str(max_number)[j]>str(i)[j]:
                break
            else:
                continue
        else:
            len_max = max(len(str(i)),len(str(max_number)))
            if [len_max-len_min]

    return max_number

def solution(numbers):
    pass

if __name__ == '__main__':
    numbers = [3,30,34]
    print(max_num(numbers))