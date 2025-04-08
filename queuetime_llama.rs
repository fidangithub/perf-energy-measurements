fn queue_time(customers: Vec<i32>, n: i32) -> i32 {
    if n >= customers.len() as i32 {
        return customers.iter().max().unwrap().to_owned();
    }

    let mut tills: Vec<i32> = vec![0; n as usize];
    for &time in customers.iter() {
        let min_till = tills.iter().enumerate().min_by_key(|&(_, &t)| t).unwrap();
        tills[min_till.0] += time;
    }
    *tills.iter().max().unwrap()
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