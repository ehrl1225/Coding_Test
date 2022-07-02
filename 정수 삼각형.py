def sum_triangle(triangle, row, column, sum_value, sum_list):
    print(1)
    if len(triangle)-1 == row:
        sum_list.append(sum_value+triangle[row][column])
        return None
    else:
        sum_value = sum_value+triangle[row][column]
        return sum_triangle(triangle, row+1,column, sum_value,sum_list), sum_triangle(triangle, row+1,column+1, sum_value,sum_list)

def solution(triangle):
    sum_list = []
    sum_triangle(triangle, 0, 0, 0, sum_list)
    answer = max(sum_list)
    return answer

if __name__ == '__main__':
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    # solution(triangle)
    sum_list = []
    sum_triangle(triangle, 0, 0, 0, sum_list)
    print(sum_list)