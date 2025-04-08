def SJF(jobs, index):
    jobs_with_indices = [(jobs[i], i) for i in range(len(jobs))]
    
    jobs_with_indices.sort()
    
    current_time = 0
    
    for job_duration, original_index in jobs_with_indices:
        current_time += job_duration
        
        if original_index == index:
            return current_time


SJF([100], 0)
SJF([3,10,20,1,2], 0)
SJF([3,10,20,1,2], 1)
SJF([3,10,20,1,2,3], 5)
SJF([3,10,20,1,2,10,10], 5)