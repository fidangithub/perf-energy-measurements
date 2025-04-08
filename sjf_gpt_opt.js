function SJF(jobs, index) {
    const targetJob = jobs[index];
    let totalTime = 0;

    for (let i = 0; i < jobs.length; i++) {
        if (
            jobs[i] < targetJob ||
            (jobs[i] === targetJob && i < index)
        ) {
            totalTime += jobs[i];
        }
    }

    return totalTime + targetJob;
}

SJF([100], 0);
SJF([3,10,20,1,2], 0);
SJF([3,10,20,1,2], 1);
SJF([3,10,20,1,2,3], 5);
SJF([3,10,20,1,2,10,10], 5);