def solution(s):
    s_index = 0
    e_index = 0
    while s_index<len(s):
        print(s_index, e_index)
        diff = e_index-s_index+1
        if s[e_index:s_index-1:-1]==s[e_index+1:e_index+1+diff]:
            s_index = e_index+1+diff
            e_index = e_index+1+diff
        elif len(s)<s_index+diff:
            return 0
        else:
            e_index+=1
    else:
        if s_index==e_index:
            return 1
        else:
            return 0

if __name__ == '__main__':
    print(solution("bcbc"))