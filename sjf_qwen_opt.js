function SJF(jobs, index) {
    let jobDetails = jobs.map((job, idx) => ({ duration: job, originalIndex: idx }));
    
    jobDetails.sort((a, b) => a.duration - b.duration || a.originalIndex - b.originalIndex);
    
    let currentTime = 0;
    let targetJob = jobDetails.find(job => job.originalIndex === index);
    
    if (!targetJob) {
        return -1;
    }
    
    for (let job of jobDetails) {
        currentTime += job.duration;
        if (job.originalIndex === index) {
            return currentTime;
        }
    }
    
    return -1;
}


SJF([100], 0);
SJF([3,10,20,1,2], 0);
SJF([3,10,20,1,2], 1);
SJF([3,10,20,1,2,3], 5);
SJF([3,10,20,1,2,10,10], 5);