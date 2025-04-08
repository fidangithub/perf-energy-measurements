def SJF(jobs, index):
    
    sorted_jobs = sorted(enumerate(jobs), key=lambda x: (x[1], x[0]))
    
    cumulative_times = [0] + [sum(job[1] for job in sorted_jobs[:i+1]) for i in range(len(sorted_jobs))]
    
    try:
        target_job_index = next(i for i, (job_idx, _) in enumerate(sorted_jobs) if job_idx == index)
    except StopIteration:
        return -1  
    
    return cumulative_times[target_job_index + 1]

SJF([100], 0)
SJF([3,10,20,1,2], 0)
SJF([3,10,20,1,2], 1)
SJF([3,10,20,1,2,3], 5)
SJF([3,10,20,1,2,10,10], 5)