def solution(array, commands):
    return [sorted(array[i[0]:i[1]+1])[i[2]-1] for i in commands]

if __name__ == '__main__':
    array =[1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    for i in commands:
        pass
    solution(array,commands)