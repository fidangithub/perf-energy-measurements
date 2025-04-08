def SJF(jobs, index):
    job_list = [(i, job) for i, job in enumerate(jobs)]
    
    sorted_jobs = sorted(job_list, key=lambda x: (x[1], x[0]))
    
    total_time = 0
    for i, job in sorted_jobs:
        total_time += job
        if i == index:
            return total_time

SJF([100], 0)
SJF([3,10,20,1,2], 0)
SJF([3,10,20,1,2], 1)
SJF([3,10,20,1,2,3], 5)
SJF([3,10,20,1,2,10,10], 5)