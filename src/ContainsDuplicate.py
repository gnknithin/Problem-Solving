from typing import List


class Solution:
    # https://leetcode.com/problems/contains-duplicate/description
    def containsDuplicate(self, nums: List[int]) -> bool:
        _duplicate = False
        _hashset: set[int] = set()
        for i in nums:
            if i in _hashset:
                _duplicate = True
                break
            _hashset.add(i)
        return _duplicate