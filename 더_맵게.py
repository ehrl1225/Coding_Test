def solution(scoville, K):
    count = 0
    scoville = sorted(scoville)
    while True:
        if len(scoville)==1:
            return -1
        scoville[0] = (scoville[0]+(scoville[1]*2))
        del scoville[1]
        scoville= sorted(scoville)
        count +=1
        if scoville[0]>=K:
            return count


if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    print(solution(scoville,K))