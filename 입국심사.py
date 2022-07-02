def search(n, times):
    time = 0
    min_n = 0
    count = lambda time: sum([time // i for i in times])
    num = lambda time: min_n + 2 ** time - 1
    while n != count(time):
        counted = count(num(time))
        if n < counted:
            min_n = num(time - 1)
            time = 0
            continue
        if n == counted:
            min_c = num(time-1)
            max_c = num(time)
            while True:
                if count((min_c+max_c)//2)<n:
                    min_c = (min_c+max_c)//2
                else:
                    max_c = (min_c+max_c)//2
                if min_c==(max_c-1):
                    return max_c
        time += 1


def solution(n, times):
    return search(n, times)

if __name__ == '__main__':
    n = 6
    times = [7,10]
    print(solution(n,times))