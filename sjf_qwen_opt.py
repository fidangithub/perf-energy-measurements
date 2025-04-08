def SJF(jobs, index):
    target_duration = jobs[index]
    current_time = 0
    
    for i, job_duration in enumerate(jobs):
        if job_duration < target_duration or (job_duration == target_duration and i <= index):
            current_time += job_duration
        if i == index:
            return current_time



SJF([100], 0)
SJF([3,10,20,1,2], 0)
SJF([3,10,20,1,2], 1)
SJF([3,10,20,1,2,3], 5)
SJF([3,10,20,1,2,10,10], 5)