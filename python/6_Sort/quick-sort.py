from sort import Strategy
from typing import List


class QuickSort(Strategy):
    def sort(self, nums: List) -> None:
        def _sort(low, high):
            if high - low < 2:
                return

            pivot = _partition(low, high)
            _sort(low, pivot)
            _sort(pivot+1, high)

        def _partition(low, high):
            pivot = high - 1

            for i in range(high - 2, -1, -1):
                if nums[i] > nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    pivot = i

            return pivot

        _sort(0, len(nums))
