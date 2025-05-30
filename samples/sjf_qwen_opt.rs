fn sjf(jobs: &[u32], index: usize) -> u32 {
    let mut jobs_with_indices: Vec<(u32, usize)> = jobs.iter().enumerate().map(|(i, &j)| (j, i)).collect();
    
    jobs_with_indices.sort_by_key(|&(length, original_index)| (length, original_index));
    
    let mut clock_cycles = 0;
    for (length, original_index) in jobs_with_indices {
        clock_cycles += length;
        if original_index == index {
            return clock_cycles;
        }
    }
    
    0
}

fn main() {
    for _ in 0..10000 {
        sjf(
            &[5, 8, 3, 20, 1, 7, 12, 6, 10, 2, 9, 15, 11, 4, 13, 14, 19, 18, 17, 16, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            10
        );
        sjf(
            &[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
            25
        );
        sjf(
            &[40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            35
        );
        sjf(
            &[5, 10, 3, 3, 20, 5, 7, 7, 7, 10, 1, 1, 1, 50, 60, 1, 3, 5, 2, 2, 10, 9, 6, 8, 4, 4, 4, 4, 3, 3, 20, 30, 10, 10, 15, 15, 5, 5, 6, 6, 12, 11, 13, 14, 8, 7, 9, 3, 2, 1],
            20
        );
        sjf(
            &[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 100],
            59
        );
    }
}
