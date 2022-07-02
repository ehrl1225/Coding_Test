def solution(participant, completion):
    participants = {}
    for i in participant:
        if i in participants:
            participants[i]+=1
        else:
            participants[i]=1
    print(participants)
    for i in completion:
        participants[i]-=1
    print(participants)
    for i in participants.keys():
        if participants[i]>0:
            return i

if __name__ == '__main__':
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    solution(participant, completion)