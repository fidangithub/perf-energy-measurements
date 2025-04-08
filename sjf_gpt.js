function SJF(jobs, index) {
    const jobsWithIndex = jobs.map((job, i) => ({ time: job, idx: i }));

    jobsWithIndex.sort((a, b) => {
        if (a.time === b.time) return a.idx - b.idx;
        return a.time - b.time;
    });

    let totalTime = 0;

    for (let job of jobsWithIndex) {
        totalTime += job.time;
        if (job.idx === index) {
            return totalTime;
        }
    }
}

SJF([100], 0);
SJF([3,10,20,1,2], 0);
SJF([3,10,20,1,2], 1);
SJF([3,10,20,1,2,3], 5);
SJF([3,10,20,1,2,10,10], 5);