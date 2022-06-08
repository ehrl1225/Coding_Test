def minus_one(n):
    for i in range(n):
        yield [-1 if i==j else 1 for j in range(n)]

def divide(n, k):
    div_list = []
    num_list = [1 for i in range(k-1)]
    max_num = n-k+1
    while num_list[0]<=max_num:
        div_list.append([i for i in num_list] + [n - sum(num_list)])
        num_list[-1]=num_list[-1]+1
        for index, num in enumerate(num_list[:0:-1]):
            real_index = k-index-2
            if num >= (n- sum(num_list[:real_index])):
                num_list[real_index-1] +=1
                num_list[real_index:] = [1 for i in range(k-real_index-1)]

    return div_list


def minus_list(n, k):
    minuses = []


if __name__ == '__main__':
    print(divide(10,4))