def heapify(arr, n, i, ascending=False):
    extreme_idx = i
    left = 2 * i + 1
    right = 2 * i + 2

    if ascending:
        # Jika ascending=True, cari yang TERKECIL (Min-Heap).
        if left < n and arr[left][0] < arr[extreme_idx][0]:
            extreme_idx = left
        if right < n and arr[right][0] < arr[extreme_idx][0]:
            extreme_idx = right
    else:
        # Jika ascending=False, cari yang TERBESAR (Max-Heap).
        if left < n and arr[left][0] > arr[extreme_idx][0]:
            extreme_idx = left
        if right < n and arr[right][0] > arr[extreme_idx][0]:
            extreme_idx = right

    if extreme_idx != i:
        arr[i], arr[extreme_idx] = arr[extreme_idx], arr[i]
        heapify(arr, n, extreme_idx, ascending)

def build_heap(arr, ascending=False):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, ascending)

def heappop(heap, ascending=False):
    n = len(heap)
    if n == 0:
        return None
    heap[0], heap[n - 1] = heap[n - 1], heap[0]
    popped = heap.pop()
    heapify(heap, len(heap), 0, ascending)
    return popped