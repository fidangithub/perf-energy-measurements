fn queue_time(customers: &[u32], n: u32) -> u32 {
    let mut q: Vec<u32> = vec![0; n as usize];
    customers.iter().for_each(|&x| {
        *q.iter_mut().min().unwrap() += x;
    });
    *q.iter().max().unwrap()
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