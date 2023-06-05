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
            left_idx = low
            right_idx = mid

            while left_idx < mid and right_idx < high:
                if nums[left_idx] <= nums[right_idx]:
                    temp.append(nums[left_idx])
                    left_idx += 1
                else:
                    temp.append(nums[right_idx])
                    right_idx += 1

            while left_idx < mid:
                temp.append(nums[left_idx])
                left_idx += 1
            while right_idx < high:
                temp.append(nums[right_idx])
                right_idx += 1

            nums[low:high] = temp

        _sort(0, len(nums))
