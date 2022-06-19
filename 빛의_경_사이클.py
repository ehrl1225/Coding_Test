def move(table, position, direction):
    row = len(table)
    col = len(table[0])
    size = [row,col]
    item = table[position[0]][position[1]]
    if item == "L":
        direction = [-1*direction[1], direction[0]]
    elif item == "R":
        direction = [direction[1], -1*direction[0]]
    position = [position[0]+direction[0], position[1]+direction[1]]
    for i in range(2):
        if position[i]<0:
            position[i] = position[i]+size[i]
        if position[i]>=size[i]:
            position[i]= position[i]-size[i]

    return position, direction

def solution(grid):
     answer = []
     return answer

if __name__ == '__main__':
    grid = ["SL","LR"]
    position = [0,0]
    direction = [1, 0]
    ways = [[position, direction]]
    while True:
        position, direction = move(grid, position, direction)
        if [position,direction] not in ways:
            ways.append([position,direction])
            print([position,direction])
        else:
            break
