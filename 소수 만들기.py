
def combination(num):
    if num<3:
        return -1
    data = [[0,1,2]]
    c = 1
    for i in range(4,num+1):
        c*=i
    for i in range(2,num-2):
        c=c//i
    for i in range(c-1):
        pre = [i for i in data[-1]]
        pre[-1]+=1
        for i in range(-1,-3,-1):
            if pre[i]==(num+i+1):
                pre[i-1]+=1
        for i in range(1,3):
            if pre[i]==(num-(2-i)):
                pre[i]=pre[i-1]+1
        data.append(pre)
    return data

def isPrimeNumber(num):
    for i in range(2,int(num**(1/2))+1):
        if num%i==0:
            return False
    else:
        return True

def solution(nums):
    return sum([1 if isPrimeNumber(sum(nums[j] for j in i)) else 0 for i in combination(len(nums))])

if __name__ == '__main__':
    nums = [1,2,3,4]
    # print(solution(nums))
    for i in combination(len(nums)):
        num = sum([nums[j] for j in i])
