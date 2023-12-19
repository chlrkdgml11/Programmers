import heapq
def solution(scoville, k):
    heap = []
    
    for sc in scoville:
        heapq.heappush(heap, sc)
        
    cnt = 0
    
    while(heap[0] < k):
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
            cnt += 1
        except :
            return -1
        
    return cnt