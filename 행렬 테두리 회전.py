def make_staight(table, x1,y1,x2,y2):
    data_list = []
    for i in range(x1,x2):
        data_list.append(table[y1][i])
    for i in range(y1,y2):
        data_list.append(table[i][x2])
    for i in range(x2,x1, -1):
        data_list.append(table[y2][i])
    for i in range(y2,y1, -1):
        data_list.append(table[i][x1])
    return data_list

def get_data(table,x1,y1,x2,y2):
    count = 0
    data_list = make_staight(table,x1,y1,x2,y2)
    data_list = [data_list[-1]]+data_list[:-1]
    def get():
        nonlocal count
        count+=1
        return data_list[count-1]
    return min(data_list),get

def rotate(table,x1,y1,x2,y2):
    min_num,data_list = get_data(table,x1,y1,x2,y2)

    for i in range(x1, x2):
        table[y1][i] = data_list()
    for i in range(y1, y2):
        table[i][x2] = data_list()
    for i in range(x2, x1,-1):
        table[y2][i] = data_list()
    for i in range(y2, y1,-1):
        table[i][x1] = data_list()
    return min_num

def make_num_table(row,col):
    table = []
    for i in range(row):
        line = []
        for j in range(col):
            line.append(i*col+j+1)
        table.append(line)
    return table

def solution(rows, columns, queries):
    answer = []
    table = make_num_table(rows,columns)
    for i in queries:
        # for j in table:
        #     print(j)
        # print()
        min_num = rotate(table, i[1]-1,i[0]-1,i[3]-1,i[2]-1)
        answer.append(min_num)
    return answer

if __name__ == '__main__':
    row, col = 100,97
    q = [[1,1,100,97]]
    test_table = make_num_table(row,col)
    print(solution(row,col,q))