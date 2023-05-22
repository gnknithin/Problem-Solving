from typing import List


class Solution:
    # https://leetcode.com/problems/product-of-array-except-self/description/
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        _answer: List[int] = list()
        _prefix = 1
        for _index in range(len(nums)):
            _answer.append(_prefix)
            _prefix = _prefix * nums[_index]
        _postfix = 1
        for _reverse_index in range(len(nums)-1,-1,-1):
            _answer[_reverse_index] = _postfix * _answer[_reverse_index]
            _postfix = _postfix * nums[_reverse_index]
        return _answer
