def solution(n, times):
    time = 0
    min_n = 0
    count = lambda time, times: sum([time // i for i in times])
    num = lambda time: min_n + 2 ** time - 1
    while n != count(time, times):
        # print(num(time))
        counted = count(num(time), times)
        if n < counted:
            min_n = num(time - 1)
            time = 0
            continue
        if n == counted:
            st = 0
            min_st = num(time - 1)
            while True:
                counted = count(min_st + 2 ** st - 1, times)
                if counted >= n:
                    min_st = min_st + 2 ** (st - 1) - 1
                    st = 0
                    continue
                if count(min_st + 2 ** st - 1, times) < count(min_st + 2 ** st, times) and count(min_st + 2 ** st,
                                                                                                 times) == n:
                    return min_st + 2 ** st
                st += 1
        time += 1


if __name__ == '__main__':
    n = 6
    times = [7,12]

    print(solution(n,times))
