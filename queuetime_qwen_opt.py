import heapq

def queue_time(customers, n):
    tills = [0] * n
    heapq.heapify(tills)
    
    for customer_time in customers:
        min_till = heapq.heappop(tills)
        heapq.heappush(tills, min_till + customer_time)
    
    return max(tills)

queue_time([], 1)
queue_time([5], 1)
queue_time([2], 5)
queue_time([1, 2, 3, 4, 5], 1)
queue_time([1, 2, 3, 4, 5], 100)
queue_time([2, 2, 3, 3, 4, 4], 2)

queue_time([5, 3, 4], 1)
queue_time([10, 2, 3, 3], 2)
queue_time([2, 3, 10, 2], 2)