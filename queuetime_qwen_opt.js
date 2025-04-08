class MinHeap {
    constructor() {
        this.heap = [];
    }

    insert(value) {
        this.heap.push(value);
        this.bubbleUp();
    }

    bubbleUp() {
        let index = this.heap.length - 1;
        while (index > 0) {
            let parentIndex = Math.floor((index - 1) / 2);
            if (this.heap[parentIndex] <= this.heap[index]) break;
            [this.heap[parentIndex], this.heap[index]] = [this.heap[index], this.heap[parentIndex]];
            index = parentIndex;
        }
    }

    extractMin() {
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop();
        const minValue = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.sinkDown();
        return minValue;
    }

    sinkDown() {
        let index = 0;
        const length = this.heap.length;
        const element = this.heap[0];

        while (true) {
            let leftChildIndex = 2 * index + 1;
            let rightChildIndex = 2 * index + 2;
            let leftChild, rightChild;
            let swap = null;

            if (leftChildIndex < length) {
                leftChild = this.heap[leftChildIndex];
                if (leftChild < element) {
                    swap = leftChildIndex;
                }
            }

            if (rightChildIndex < length) {
                rightChild = this.heap[rightChildIndex];
                if (
                    (swap === null && rightChild < element) ||
                    (swap !== null && rightChild < leftChild)
                ) {
                    swap = rightChildIndex;
                }
            }

            if (swap === null) break;
            this.heap[index] = this.heap[swap];
            this.heap[swap] = element;
            index = swap;
        }
    }

    peek() {
        return this.heap[0];
    }

    size() {
        return this.heap.length;
    }
}

function queueTime(customers, n) {
    const tills = new MinHeap();

    for (let i = 0; i < n; i++) {
        tills.insert(0);
    }

    for (let time of customers) {
        let minTime = tills.extractMin();
        tills.insert(minTime + time);
    }

    return tills.peek();
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
