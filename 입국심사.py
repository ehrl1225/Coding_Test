def count(time,times):
    return sum([time//i for i in times])

def search(min_n,n,times):
    time = 1
    while n>count(min_n+time-1, times):
        print(min_n+time-1)
        counted=count(min_n+time-1,times)
        if n>counted:
            min_n=min_n+time-1
        if n == counted:
            break
        time*=2
    if n==count(min_n+time-1, times):
        return min_n+time-1
    return search(min_n,n,times)

def solution(n,times):
    answer = search(0,n,times)
    return answer

if __name__ == '__main__':
    n=6
    times = [7,10]
    # print(count(10,times))
    print(solution(n,times))