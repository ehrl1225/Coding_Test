
def solution(N,stages):
    answer = [i +1 for i in range(N)]
    trials = [0 for i in range(N)]
    fails = [0 for i in range(N)]
    for i in stages:
        for j in range(i):
            if j<N:
                trials[j]+=1
    for i in stages:
        if i<=N:
            fails[i-1]+=1
    return sorted(answer, key=lambda num: 0 if trials[num-1]==0 else fails[num-1]/trials[num-1], reverse=True)

if __name__ == '__main__':
    N=5
    stages =[2, 1, 2, 6, 2, 4, 3, 3]
    # solution(N,stages)
    print(solution(N,stages))