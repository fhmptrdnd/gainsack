def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left][0] > arr[largest][0]:
        largest = left
    if right < n and arr[right][0] > arr[largest][0]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heappop(heap):
    n = len(heap)
    if n == 0:
        return None
    heap[0], heap[n - 1] = heap[n - 1], heap[0]
    popped = heap.pop()
    heapify(heap, len(heap), 0)
    return popped
