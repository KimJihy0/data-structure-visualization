from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import importlib


class Sort():
    def __init__(self, strategy: Strategy, nums: List) -> None:
        self._strategy = strategy
        self._nums = nums

    def run(self) -> None:
        print(self._nums)
        self._strategy.sort(self._nums)
        print(self._nums)


class Strategy:
    @abstractmethod
    def sort(self, nums: List):
        pass


if __name__ == "__main__":
    InsertionSort = importlib.import_module("insertion-sort").InsertionSort
    SelectionSort = importlib.import_module("selection-sort").SelectionSort
    BubbleSort = importlib.import_module("bubble-sort").BubbleSort
    HeapSort = importlib.import_module("heap-sort").HeapSort
    MergeSort = importlib.import_module("merge-sort").MergeSort
    QuickSort = importlib.import_module("quick-sort").QuickSort

    nums = [8, 1, 4, 9, 0, 3, 5, 2, 7, 6]
    s = Sort(QuickSort(), nums)
    s.run()
