from sort import Strategy
from typing import List


class InsertionSort(Strategy):
    def sort(self, nums: List) -> None:
        for end in range(1, len(nums)):
            i = end
            while i > 0 and nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                i -= 1
