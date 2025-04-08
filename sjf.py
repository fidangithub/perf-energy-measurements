def SJF(jobs, index):
    return sum(j for i, j in enumerate(jobs)
                 if j < jobs[index] or (j == jobs[index] and i <= index))

SJF([100], 0)
SJF([3,10,20,1,2], 0)
SJF([3,10,20,1,2], 1)
SJF([3,10,20,1,2,3], 5)
SJF([3,10,20,1,2,10,10], 5)