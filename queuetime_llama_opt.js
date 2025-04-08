class PriorityQueue {
    constructor() {
        this.heap = [];
    }

    add(value) {
        this.heap.push(value);
        this.heap.sort((a, b) => a - b);
    }

    remove() {
        return this.heap.shift();
    }

    getMin() {
        return this.heap[0];
    }

    isEmpty() {
        return this.heap.length === 0;
    }
}

function queueTime(customers, n) {
    let tills = new PriorityQueue();

    for (let i = 0; i < n; i++) {
        tills.add(0);
    }

    for (let time of customers) {
        let minTill = tills.remove();

        tills.add(minTill + time);
    }

    let max = 0;
    while (!tills.isEmpty()) {
        max = Math.max(max, tills.remove());
    }

    return max;
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
