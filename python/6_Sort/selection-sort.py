from sort import Strategy
from typing import List


class SelectionSort(Strategy):
    def sort(self, nums: List) -> None:
        for i in range(len(nums)-1):
            idx = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[idx]:
                    idx = j
            nums[idx], nums[i] = nums[i], nums[idx]
