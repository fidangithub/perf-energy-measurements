function SJF(jobs, index){
  return jobs.reduce((a,b,i)=>a+(b<jobs[index]||(b==jobs[index]&&i<=index) ? b:0),0);
}

SJF([100], 0);
SJF([3,10,20,1,2], 0);
SJF([3,10,20,1,2], 1);
SJF([3,10,20,1,2,3], 5);
SJF([3,10,20,1,2,10,10], 5);