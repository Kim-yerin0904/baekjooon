import heapq
def solution(operations):
    heap =[]
    for i in operations:
        if i[:2] ==  "I ":
            i=i.replace("I ","")
            i= int(i)
            heapq.heappush(heap,i)
        elif i =="D 1" and len(heap)>0:
            a = max(heap)
            del heap[heap.index(a)]
        elif i =="D -1" and len(heap)>0:
            heapq.heappop(heap)
    if len(heap) > 0:
        return [max(heap),heap[0]]
    else:
        return [0,0]
