def max_num(numbers):
    max_number = numbers[0]
    max_index = 0
    for index, i in enumerate(numbers[1:]):
        len_min = min(len(str(i)),len(str(max_number)))
        for j in range(len_min):
            if str(max_number)[j]<str(i)[j]:
                max_number=i
                max_index = index + 1
                break
            elif str(max_number)[j]>str(i)[j]:
                break
            else:
                continue
        else:
            len_max = max(len(str(i)),len(str(max_number)))
            differ_len=len_max- len_min
            if differ_len!=0:
                if len(str(i))>len(str(max_number)):
                    if str(i)[len_min]>str(i)[0]:
                        max_number=i
                        max_index = index + 1
                elif len(str(i))<len(str(max_number)):
                    if str(max_number)[len_min]<str(max_number)[0]:
                        max_number=i
                        max_index = index+1

    return max_number,max_index

def solution(numbers):
    text = ""
    for i in range(len(numbers)):
        max_number, max_index = max_num(numbers)
        del numbers[max_index]
        text+=str(max_number)
    return text

if __name__ == '__main__':
    numbers = [3, 30, 34, 5, 9]
    for i in range(5):
        max_number, max_index = max_num(numbers)
        del numbers[max_index]
        print(max_number)