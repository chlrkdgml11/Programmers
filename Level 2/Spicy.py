def solution(scoville, K):
    result = 0
    before = 0

    while(min(scoville) < K):
        before = min(scoville)
        
        scoville.sort()

        scoville.append(scoville[0] + scoville[1] * 2)

        scoville.remove(scoville[0])
        scoville.remove(scoville[0])
        scoville.sort()
        
        if before >= min(scoville) or len(scoville < 2):
            return -1

        result += 1

    return result

solution([1, 2, 3, 9, 10, 12], 7)