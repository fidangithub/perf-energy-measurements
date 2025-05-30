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

const tests = () => {
   SJF(
    [5, 8, 3, 20, 1, 7, 12, 6, 10, 2, 9, 15, 11, 4, 13, 14, 19, 18, 17, 16, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    10
  );
  SJF(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    25
  );
  SJF(
    [40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    35
  );
  SJF(
    [5, 10, 3, 3, 20, 5, 7, 7, 7, 10, 1, 1, 1, 50, 60, 1, 3, 5, 2, 2, 10, 9, 6, 8, 4, 4, 4, 4, 3, 3, 20, 30, 10, 10, 15, 15, 5, 5, 6, 6, 12, 11, 13, 14, 8, 7, 9, 3, 2, 1],
    20
  );
  SJF(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 100],
    59
  );
}

let warmup = () => {
  for (let i = 0; i < 500; i++) tests();
  if (global.gc) global.gc(); // final GC cleanup
}

let runTests = () => {
  for (let i = 0; i < 10000; i++) {
    tests();
  }
  if (global.gc) global.gc(); // pre-benchmark GC
}

if (process.env.MEASURE === "true") {
  runTests(); 
} else {
  warmup();
  process.exit(0);
}
