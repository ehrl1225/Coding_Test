def minus_one(n):
    matrix = []
    for i in range(n):
        matrix.append([-1 if i==j else 1 for j in range(n)])
    return matrix

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
    if k==1:
        return minus_one(n)
    else:
        for i in divide(n,k):
            matrix = []
            for j in i[:-1]:
                matrix += minus_one(j)[-1]

            for j in minus_one(i[-1]):
                minuses.append([i for i in matrix]+j)
        return minuses

def multiply(numbers,target, n,k):
    count = 0
    for i in minus_list(n,k):
        if sum([numbers[j]*i[j] for j in range(len(numbers))]) == target:
            count+=1
    return count

def solution(numbers, target):
    n = len(numbers)
    answer = 0
    for i in range(1,n):
        answer += multiply(numbers,target,n,i)
    return answer

if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers,target))