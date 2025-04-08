def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)

queue_time([], 1)
queue_time([5], 1)
queue_time([2], 5)
queue_time([1, 2, 3, 4, 5], 1)
queue_time([1, 2, 3, 4, 5], 100)
queue_time([2, 2, 3, 3, 4, 4], 2)

queue_time([5, 3, 4], 1)
queue_time([10, 2, 3, 3], 2)
queue_time([2, 3, 10, 2], 2)