def solution(participant, competion):
    dict = {}
    sum = 0

    for i in range(len(participant)):
        dict[participant[i]] = hash(participant[i])
        sum += hash(participant[i])

    for j in range(len(competion)):
        sum -= hash(competion[i])

    return dict[sum]