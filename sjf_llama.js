function SJF(jobs, index) {
    const jobsCopy = jobs.slice();

    let currentCc = 0;
    let totalCc = 0;

    while (true) {
        let shortestJobIndex = -1;
        let shortestJobCc = Infinity;
        for (let i = 0; i < jobsCopy.length; i++) {
            if (jobsCopy[i] > 0 && jobsCopy[i] < shortestJobCc) {
                shortestJobIndex = i;
                shortestJobCc = jobsCopy[i];
            }
        }

        if (shortestJobIndex === index) {
            totalCc += jobsCopy[shortestJobIndex];
            jobsCopy[shortestJobIndex] = 0;
            break;
        }

        currentCc = Math.min(currentCc + jobsCopy[shortestJobIndex], jobsCopy[shortestJobIndex]);
        totalCc += currentCc;
        jobsCopy[shortestJobIndex] -= currentCc;
        currentCc = 0;
    }

    return totalCc;
}

SJF([100], 0);
SJF([3,10,20,1,2], 0);
SJF([3,10,20,1,2], 1);
SJF([3,10,20,1,2,3], 5);
SJF([3,10,20,1,2,10,10], 5);