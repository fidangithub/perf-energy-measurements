function getShortestJobIndex(jobs) {
    let shortestJobIndex = -1;
    let shortestJobCc = Infinity;

    for (let i = 0; i < jobs.length; i++) {
        if (jobs[i] > 0 && jobs[i] < shortestJobCc) {
            shortestJobIndex = i;
            shortestJobCc = jobs[i];
        }
    }

    return shortestJobIndex;
}

function SJF(jobs, index) {
    const jobsCopy = [...jobs];

    let totalCc = 0;

    while (jobsCopy[index] > 0) {
        const shortestJobIndex = getShortestJobIndex(jobsCopy);

        if (shortestJobIndex === index) {
            totalCc += jobsCopy[shortestJobIndex];
            jobsCopy[shortestJobIndex] = 0;
        } else {
            totalCc += jobsCopy[shortestJobIndex];
            jobsCopy[shortestJobIndex] = 0;
        }
    }

    return totalCc;
}

SJF([100], 0);
SJF([3,10,20,1,2], 0);
SJF([3,10,20,1,2], 1);
SJF([3,10,20,1,2,3], 5);
SJF([3,10,20,1,2,10,10], 5);