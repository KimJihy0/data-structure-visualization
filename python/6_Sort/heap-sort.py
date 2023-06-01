from sort import Strategy
from typing import List


class HeapSort(Strategy):
    def sort(self, nums: List) -> None:
        def heapify(heap, idx, size):
            max_idx = idx
            left_idx = idx * 2 + 1
            right_idx = idx * 2 + 2

            if left_idx < size and heap[left_idx] > heap[max_idx]:
                max_idx = left_idx
            if right_idx < size and heap[right_idx] > heap[max_idx]:
                max_idx = right_idx

            if max_idx != idx:
                heap[idx], heap[max_idx] = heap[max_idx], heap[idx]
                heapify(heap, max_idx, size)

        size = len(nums)
        for i in range(size // 2 - 1, -1, -1):
            heapify(nums, i, size)
        for i in range(size - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(nums, 0, i)
