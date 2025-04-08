import heapq

def queue_time(customers, n):
    if n == 1:
        return sum(customers)
    if not customers:
        return 0

    q = [0] * n
    for time in customers:
        heapq.heapreplace(q, heapq.heappushpop(q, time + heapq.heappop(q)))
    return max(q)


queue_time([], 1)
queue_time([5], 1)
queue_time([2], 5)
queue_time([1, 2, 3, 4, 5], 1)
queue_time([1, 2, 3, 4, 5], 100)
queue_time([2, 2, 3, 3, 4, 4], 2)

queue_time([5, 3, 4], 1)
queue_time([10, 2, 3, 3], 2)
queue_time([2, 3, 10, 2], 2)