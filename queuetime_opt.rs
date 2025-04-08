use std::collections::BinaryHeap;
use std::cmp::Reverse;

fn queue_time(customers: &[u32], n: u32) -> u32 {
    let mut heap: BinaryHeap<Reverse<u32>> = vec![Reverse(0); n as usize].into();

    for &time in customers {
        let Reverse(min_time) = heap.pop().unwrap();
        heap.push(Reverse(min_time + time));
    }

    heap.into_iter().map(|Reverse(t)| t).max().unwrap_or(0)
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