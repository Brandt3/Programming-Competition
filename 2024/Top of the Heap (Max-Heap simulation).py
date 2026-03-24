# =============================================================================
# Problem 7 — Top of the Heap (Max-Heap simulation)
# =============================================================================

def solve_heap():
    n = int(input())
    heap = []

    def enqueue(val):
        heap.append(val)
        # Percolate up
        i = len(heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if heap[i] > heap[parent]:
                heap[i], heap[parent] = heap[parent], heap[i]
                i = parent
            else:
                break

    def dequeue():
        if not heap:
            return
        if len(heap) == 1:
            heap.pop()
            return
        heap[0] = heap.pop()
        # Percolate down
        i = 0
        while True:
            left  = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left  < len(heap) and heap[left]  > heap[largest]:
                largest = left
            if right < len(heap) and heap[right] > heap[largest]:
                largest = right
            if largest == i:
                break
            heap[i], heap[largest] = heap[largest], heap[i]
            i = largest

    for _ in range(n):
        line = input().split()
        if line[0] == 'E':
            enqueue(int(line[1]))
        else:
            dequeue()

    print(len(heap))
    for val in heap:
        print(val)

solve_heap()