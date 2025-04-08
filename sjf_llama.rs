fn sjf(jobs: Vec<i32>, index: usize) -> i32 {
    let mut jobs = jobs
       .into_iter()
       .enumerate()
       .map(|(i, job)| (i, job))
       .collect::<Vec<_>>();

    let mut current_cc = 0;
    let mut finished = vec![];

    while jobs.len() > 0 {
        jobs.sort_by_key(|&(_, job)| job);

        let (i, mut job) = jobs.remove(0);

        while job > 0 {
            job -= 1;

            current_cc += 1;

            if job == 0 {
                finished.push(i);
            }
        }
    }

    finished
       .into_iter()
       .enumerate()
       .find(|&(_, i)| i == index)
       .map(|(cc, _)| cc as i32 + 1)
       .unwrap()
}

sjf(&[100], 0)
sjf(&[3,10,20,1,2], 0)
sjf(&[3,10,20,1,2], 1)
sjf(&[3,10,20,1,2,3], 5)
sjf(&[3,10,20,1,2,10,10], 5)