
def target_count(numbers, target, index=0, sum_n=0):
    if index == len(numbers):
        if sum_n==target:
            return 1
        else:
            return 0
    else:
        plus = target_count(numbers,target,index+1, sum_n+numbers[index])
        minus = target_count(numbers,target, index+1, sum_n-numbers[index])
        return plus+minus

if __name__ == '__main__':
    numbers = [4, 1, 2, 1]
    target = 4
    print(target_count(numbers,target))