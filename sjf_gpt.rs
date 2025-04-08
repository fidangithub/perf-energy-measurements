fn sjf(jobs: Vec<usize>, index: usize) -> usize {
    let target_job = jobs[index];
    let mut time = 0;

    for (i, &job) in jobs.iter().enumerate() {
        if job < target_job || (job == target_job && i < index) {
            time += job;
        }
    }

    time + target_job
}

sjf(&[100], 0)
sjf(&[3,10,20,1,2], 0)
sjf(&[3,10,20,1,2], 1)
sjf(&[3,10,20,1,2,3], 5)
sjf(&[3,10,20,1,2,10,10], 5)