function queueTime(customers, n) {
    let tills = new Array(n).fill(0);
    
    for (let time of customers) {
        let minIndex = 0;
        for (let i = 1; i < n; i++) {
            if (tills[i] < tills[minIndex]) {
                minIndex = i;
            }
        }
        tills[minIndex] += time;
    }
    
    return Math.max(...tills);
}


queueTime([], 1);
queueTime([5], 1);
queueTime([2], 5);
queueTime([1,2,3,4,5], 1);
queueTime([1,2,3,4,5], 100);
queueTime([2,2,3,3,4,4], 2);

queueTime([5,3,4], 1);
queueTime([10,2,3,3], 2);
queueTime([2,3,10,2], 2);
