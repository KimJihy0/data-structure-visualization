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
            pivot = low
            left = low + 1
            right = high - 1

            while left <= right:
                while left < high and nums[left] < nums[pivot]:
                    left += 1
                while right > low and nums[right] > nums[pivot]:
                    right -= 1

                if left > right:
                    nums[right], nums[pivot] = nums[pivot], nums[right]
                else:
                    nums[left], nums[right] = nums[right], nums[left]

            return right

        _sort(0, len(nums))
