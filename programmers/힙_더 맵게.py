import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while (len(scoville) > 1):
        if scoville[0] < K:
            a=heapq.heappop(scoville)
            b=heapq.heappop(scoville)
            new_food =a + (b*2)
            heapq.heappush(scoville,new_food)
            answer += 1
        else:
            break
    if scoville[0] < K:
        return -1
    else:
        return answer
