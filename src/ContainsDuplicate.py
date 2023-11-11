from typing import List, Set


class Solution:
    # https://leetcode.com/problems/contains-duplicate/description
    def containsDuplicate(self, nums: List[int]) -> bool:
        _duplicate = False
        _hashset: Set[int] = set()
        for element in nums:
            if element in _hashset:
                _duplicate = True
                break
            _hashset.add(element)
        return _duplicate
