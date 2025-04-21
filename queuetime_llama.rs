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

fn main() {
    for _ in 0..1000 {
        queue_time(&[], 1);
        queue_time(&[5], 1);
        queue_time(&[2], 5);

        queue_time(
            &[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
             31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
             41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 
            1
        );

        queue_time(
            &[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 
            100
        );

        queue_time(
            &[2, 2, 3, 3, 4, 4, 5, 5, 6, 6,
            2, 2, 3, 3, 4, 4, 5, 5, 6, 6,
            2, 2, 3, 3, 4, 4, 5, 5, 6, 6,
            2, 2, 3, 3, 4, 4, 5, 5, 6, 6,
            2, 2, 3, 3, 4, 4, 5, 5, 6, 6], 
            5
        );

        queue_time(
            &[5, 3, 4, 6, 7, 8, 2, 3, 9, 1, 4, 5, 6, 3, 2, 1, 5, 6, 4, 3,
            7, 8, 6, 5, 4, 3, 9, 10, 8, 6,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
            3
        );

        queue_time(
            &[10, 2, 3, 3, 7, 8, 9, 5, 4, 3, 2, 1, 6, 7, 8, 5, 4, 3, 9, 10], 
            4
        );

        queue_time(
            &[2, 3, 10, 2, 5, 3, 1, 4, 6, 2, 3, 7, 4, 5, 6, 8, 9, 10, 2, 1,
             1, 2, 3, 4, 5, 3, 2, 1, 2, 4], 
            2
        );
    }
}