def move(grid, position, direction):
    row = len(grid)
    col = len(grid[0])
    size = [row,col]
    item = grid[position[0]][position[1]]
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

def is_in_cycles(cycles, cycle):
    for i in cycles:
        for j in cycle:
            if j in i:
                return True
    else:
        return False

def one_cycle(grid,cycles, position, direction):
    ways = [[position, direction]]
    while True:
        position, direction = move(grid, position, direction)
        if [position,direction] not in ways:
            ways.append([position,direction])
        else:
            break
    return ways[ways.index([position,direction]):]

def find_cycle(grid):
    cycles = []
    row = len(grid)
    column = len(grid[0])
    for y in range(row):
        for x in range(column):
            for d in range(-1,2,2):
                y_cycle = one_cycle(grid,cycles,[y,x],[d,0])
                x_cycle = one_cycle(grid,cycles, [y, x], [0, d])
                if not is_in_cycles(cycles,y_cycle):
                    cycles.append(y_cycle)
                if not is_in_cycles(cycles,x_cycle):
                    cycles.append(x_cycle)
    return cycles

def solution(grid):
     answer = [len(i) for i in find_cycle(grid)]
     return answer

if __name__ == '__main__':
    grid = ["SL","LR"]
    # position = [1,0]
    # direction = [1, 0]
    # ways = [[position, direction]]
    # while True:
    #     position, direction = move(grid, position, direction)
    #     if [position,direction] not in ways:
    #         ways.append([position,direction])
    #         print([position,direction])
    #     else:
    #         break
    # print(len(ways))
    print([len(i) for i in find_cycle(grid)])