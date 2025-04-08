fn sjf(jobs: &[usize], index: usize) -> usize {
    let duration = jobs[index];
    jobs.iter().enumerate().fold(0, |acc, (i, &d)| {
        if d < duration || (d == duration && i <= index) {
            acc + d
        } else {
            acc
        }
    })
}

sjf(&[100], 0)
sjf(&[3,10,20,1,2], 0)
sjf(&[3,10,20,1,2], 1)
sjf(&[3,10,20,1,2,3], 5)
sjf(&[3,10,20,1,2,10,10], 5)