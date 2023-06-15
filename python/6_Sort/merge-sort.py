from sort import Strategy
from typing import List


class MergeSort(Strategy):
    def sort(self, nums: List) -> None:
        def _sort(low, high):
            if high - low < 2:
                return

            mid = (low + high) // 2
            _sort(low, mid)
            _sort(mid, high)
            _merge(low, mid, high)

        def _merge(low, mid, high):
            temp = []
            left = low
            right = mid

            while left < mid and right < high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1

            while left < mid:
                temp.append(nums[left])
                left += 1
            while right < high:
                temp.append(nums[right])
                right += 1

            nums[low:high] = temp

        _sort(0, len(nums))
