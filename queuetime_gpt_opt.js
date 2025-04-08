function queueTime(customers, n) {
  const tills = Array(n).fill(0);

  for (const time of customers) {
    let i = 0;
    for (let j = 1; j < n; j++) {
      if (tills[j] < tills[i]) i = j;
    }
    tills[i] += time;
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
