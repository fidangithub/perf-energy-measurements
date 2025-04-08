class MinHeap {
  constructor(size) {
    this.heap = new Array(size).fill(0);
  }

  push(val) {
    this.heap.push(val);
    this._bubbleUp();
  }

  popPush(val) {
    this.heap[0] += val;
    this._sinkDown(0);
  }

  max() {
    return Math.max(...this.heap);
  }

  _bubbleUp() {
    let idx = this.heap.length - 1;
    while (idx > 0) {
      let parent = Math.floor((idx - 1) / 2);
      if (this.heap[parent] <= this.heap[idx]) break;
      [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
      idx = parent;
    }
  }

  _sinkDown(idx) {
    let length = this.heap.length;
    while (true) {
      let left = 2 * idx + 1;
      let right = 2 * idx + 2;
      let smallest = idx;

      if (left < length && this.heap[left] < this.heap[smallest]) smallest = left;
      if (right < length && this.heap[right] < this.heap[smallest]) smallest = right;

      if (smallest === idx) break;
      [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
      idx = smallest;
    }
  }
}

function queueTime(customers, n) {
  if (n === 0) return 0;
  const heap = new MinHeap(n);
  for (let t of customers) {
    heap.popPush(t);
  }
  return heap.max();
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
