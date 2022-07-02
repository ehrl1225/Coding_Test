
def solution(board, moves):
    answer = 0
    out = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]:
                if len(out)==0:
                    out.append(board[j][i-1])
                elif out[-1]==board[j][i-1]:
                    del out[-1]
                    answer +=1
                else:
                    out.append(board[j][i-1])
                board[j][i-1]= 0
                break
    return answer*2

if __name__ == '__main__':
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board, moves))