def SJF(jobs, index):
    target_job = (index, jobs[index])
    return sum(job for i, job in sorted(enumerate(jobs), key=lambda x: (x[1], x[0])) if (i, job) <= target_job)


SJF([100], 0)
SJF([3,10,20,1,2], 0)
SJF([3,10,20,1,2], 1)
SJF([3,10,20,1,2,3], 5)
SJF([3,10,20,1,2,10,10], 5)