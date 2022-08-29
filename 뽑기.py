import random

def solution(event):
    # random_number = random.randint(1,1000)
    random_number =1
    sum_events = [sum(int(j*10) for j in event[:i+1]) for i in range(len(event))]
    print(sum_events)
    for index in range(len(sum_events)):
        if sum_events[index]<random_number<=sum_events[index+1]:
            print(event[index+1], index+1)
            break
        elif 1==random_number:
            print(event[0],0)
            break

if __name__ == '__main__':
    event = [10,8,4.3,15,15,2.2,2.2,4.1,10,10,3.1,3.1,13]
    solution(event)
