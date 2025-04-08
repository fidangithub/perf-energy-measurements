def SJF(jobs, index):
    job_list = [(i, job) for i, job in enumerate(jobs)]
    
    sorted_jobs = sorted(job_list, key=lambda x: (x[1], x[0]))
    
    total_time = 0
    target_index = index
    
    for i, (job_idx, job_cc) in enumerate(sorted_jobs):
        if job_idx == target_index:
            return total_time + job_cc
        
        total_time += job_cc
    
    return -1

SJF([100], 0)
SJF([3,10,20,1,2], 0)
SJF([3,10,20,1,2], 1)
SJF([3,10,20,1,2,3], 5)
SJF([3,10,20,1,2,10,10], 5)