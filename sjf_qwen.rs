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
    sjf(&[100], 0)
    sjf(&[3,10,20,1,2], 0)
    sjf(&[3,10,20,1,2], 1)
    sjf(&[3,10,20,1,2,3], 5)
    sjf(&[3,10,20,1,2,10,10], 5)
}