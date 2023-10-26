from typing import List


class Solution:
    # Given an integer array nums, return true if any value appears at least twice in the array, and return false if
    # every element is distinct.

    @staticmethod
    def contains_duplicate(nums: List[int]) -> bool:
        numbers = set()
        for n in nums:
            if n in numbers:
                return True
            numbers.add(n)
        return False
