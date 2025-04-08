use std::collections::BinaryHeap;
use std::cmp::Reverse;

fn queue_time(customers: &[u32], n: usize) -> u32 {
    let mut tills = BinaryHeap::with_capacity(n);
    for _ in 0..n {
        tills.push(Reverse(0));
    }

    for &time in customers {
        let Reverse(mut free_time) = tills.pop().unwrap();
        free_time += time;
        tills.push(Reverse(free_time));
    }

    tills.into_iter().map(|Reverse(time)| time).max().unwrap()
}


queue_time(&[], 1);
queue_time(&[5], 1);
queue_time(&[2], 5);
queue_time(&[1,2,3,4,5], 1);
queue_time(&[1,2,3,4,5], 100);
queue_time(&[2,2,3,3,4,4], 2);

queue_time(&[5,3,4], 1);
queue_time(&[10,2,3,3], 2);
queue_time(&[2,3,10,2], 2);