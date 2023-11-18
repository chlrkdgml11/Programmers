def solution(participant, competion):
    
    dict = {}
    sum = 0
    
    for part in participant:
        dict[hash(part)] = part
        sum += hash(part)
        
    for comp in competion:
        sum -= hash(comp)

    return dict[sum]