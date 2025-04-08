function SJF(jobs, index) {
  const targetJob = jobs[index];
  return jobs.reduce((total, job, i) =>
    job < targetJob || (job === targetJob && i <= index) ? total + job : total
  , 0);
}


SJF([100], 0);
SJF([3,10,20,1,2], 0);
SJF([3,10,20,1,2], 1);
SJF([3,10,20,1,2,3], 5);
SJF([3,10,20,1,2,10,10], 5);