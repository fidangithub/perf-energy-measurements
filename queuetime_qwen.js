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


let runTests = () => {
  queueTime([], 1);
  queueTime([5], 1);
  queueTime([2], 5);

  queueTime(
    [
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
      21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
      31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
      41, 42, 43, 44, 45, 46, 47, 48, 49, 50
    ],
    1
  );

  queueTime(
    [
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
      11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ],
    100
  );

  queueTime(
    [
      2, 2, 3, 3, 4, 4, 5, 5, 6, 6,
      2, 2, 3, 3, 4, 4, 5, 5, 6, 6,
      2, 2, 3, 3, 4, 4, 5, 5, 6, 6,
      2, 2, 3, 3, 4, 4, 5, 5, 6, 6,
      2, 2, 3, 3, 4, 4, 5, 5, 6, 6
    ],
    5
  );

  queueTime(
    [
      5, 3, 4, 6, 7, 8, 2, 3, 9, 1, 4, 5, 6, 3, 2, 1, 5, 6, 4, 3,
      7, 8, 6, 5, 4, 3, 9, 10, 8, 6,
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ],
    3
  );

  queueTime(
    [
      10, 2, 3, 3, 7, 8, 9, 5, 4, 3, 2, 1, 6, 7, 8, 5, 4, 3, 9, 10
    ],
    4
  );

  queueTime(
    [
      2, 3, 10, 2, 5, 3, 1, 4, 6, 2, 3, 7, 4, 5, 6, 8, 9, 10, 2, 1,
      1, 2, 3, 4, 5, 3, 2, 1, 2, 4
    ],
    2
  );
}

if (process.env.MEASURE !== "true") {
  for (let i = 0; i < 500; i++) runTests();
  if (global.gc) global.gc();
  process.exit(0);
}

if (global.gc) global.gc();
for (let i = 0; i < 10000; i++) {
  runTests();
}
if (global.gc) global.gc();