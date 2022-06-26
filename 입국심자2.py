def search(n):
    i = 0
    min_n=0
    num = lambda  : 2**i+min_n
    while n!=num():
        print(num())
        if n < num():
            min_n= 2**(i-1)+min_n
            i=0
            continue
        if n==num():
            return num()

        i+=1

def solution(n, times):
    time = 1
    count = lambda time : sum([time//i for i in times])
    while True:
        if count(time)==n:
            return time
        time+=1

if __name__ == '__main__':
    print(search(5))