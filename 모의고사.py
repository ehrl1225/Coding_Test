
def solution(answers):
    math_looser = [[1,2,3,4,5],
                   [2,1,2,3,2,4,2,5],
                   [3,3,1,1,2,2,4,4,5,5]]
    answer = [0 for i in range(3)]
    for index, j in enumerate(answers):
        for i in range(3):
            if math_looser[i][index%(len(math_looser[i]))]==j:
                answer[i]+=1
    max_answer = max(answer)
    max_answers = []
    for index, i in enumerate(answer):
        if i==max_answer:
            max_answers.append(index+1)
    return sorted(max_answers)

if __name__ == '__main__':
    answers = [1,2,3,4,5]
    solution(answers)