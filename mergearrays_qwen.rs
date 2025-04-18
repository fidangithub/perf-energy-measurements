fn merge_arrays(arr1: &[i32], arr2: &[i32]) -> Vec<i32> {
    fn is_ascending(arr: &[i32]) -> bool {
        arr.windows(2).all(|w| w[0] <= w[1])
    }

    let ascending1 = is_ascending(arr1);
    let ascending2 = is_ascending(arr2);

    let iter1 = if ascending1 { arr1.iter() } else { arr1.iter().rev() };
    let iter2 = if ascending2 { arr2.iter() } else { arr2.iter().rev() };

    let mut merged: Vec<i32> = iter1.chain(iter2).cloned().collect();
    merged.sort_unstable(); 
    merged.dedup();
 
    merged
}

fn main() {
    merge_arrays(&[1,2,3,4], &[5,6,7,8]);
    merge_arrays(&[1,3,5,7,9], &[10,8,6,4,2]);
    merge_arrays(&[1,3,5,7,9,11,12], &[1,2,3,4,5,10,12]);
    merge_arrays(&[5,6,7,8,9,10], &[20,18,15,14,13,12,11,4,3,2]);
    merge_arrays(&[45,30,20,15,12,5], &[9,10,18,25,35,50]);
    merge_arrays(&[-8,-3,-2,4,5,6,7,15,42,90,134], &[216,102,74,32,8,2,0,-9,-13]);
    merge_arrays(&[-100,-27,-8,5,23,56,124,325], &[-34,-27,6,12,25,56,213,325,601]);
    merge_arrays(&[18,7,2,0,-22,-46,-103,-293], &[-300,-293,-46,-31,-5,0,18,19,74,231]);
    merge_arrays(&[105,73,-4,-73,-201], &[-201,-73,-4,73,105]);
    merge_arrays(&[10,8,6,4,2], &[9,7,5,3,1]);
    merge_arrays(&[-20,35,36,37,39,40], &[-10,-5,0,6,7,8,9,10,25,38,50,62]);
    merge_arrays(&[], &[]);
    merge_arrays(&[1,2,3], &[]);
    merge_arrays(&[], &[5,4,3,2,1]);
}