from sort import Strategy
from typing import List


class BubbleSort(Strategy):
    def sort(self, nums: List) -> None:
        for i in range(len(nums)-1, 0, -1):
            swapped = False
            for j in range(i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if not swapped:
                break
