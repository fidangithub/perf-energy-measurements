fn sjf(jobs: &[usize], index: usize) -> usize {
    let duration = jobs[index];
    jobs.iter().enumerate()
        .filter(|&(i, d)| (*d < duration) || (*d == duration && i <= index))
        .map(|(_, d)| d)
        .sum()
}

fn main() {
    sjf(&[100], 0);
    sjf(&[3, 10, 20, 1, 2], 0);
    sjf(&[3, 10, 20, 1, 2], 1);
    sjf(&[3, 10, 20, 1, 2, 3], 5);
    sjf(&[3, 10, 20, 1, 2, 10, 10], 5);
}