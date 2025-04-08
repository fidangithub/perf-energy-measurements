def SJF(jobs, index):
    target = jobs[index]
    return sum(j for i, j in zip(range(index + 1), jobs[:index + 1]) if j <= target) + \
           sum(j for j in jobs[index + 1:] if j < target)


SJF([100], 0)
SJF([3,10,20,1,2], 0)
SJF([3,10,20,1,2], 1)
SJF([3,10,20,1,2,3], 5)
SJF([3,10,20,1,2,10,10], 5)