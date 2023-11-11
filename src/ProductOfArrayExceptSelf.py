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
        for _reverse_index in range(len(nums)-1, -1, -1):
            _answer[_reverse_index] = _postfix * _answer[_reverse_index]
            _postfix = _postfix * nums[_reverse_index]
        return _answer


class AnotherSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        _size = len(nums)
        _prefix: List[int] = [0]*_size
        _postfix: List[int] = [0]*_size
        _prefix_value = 1
        _postfix_value = 1
        i = 0
        while (i < _size):
            _prefix[i] = _prefix_value
            _prefix_value = _prefix_value * nums[i]
            j = _size-1-i
            _postfix[j] = _postfix_value
            _postfix_value = _postfix_value * nums[j]
            i += 1
        return [_postfix[_index]*_prefix[_index] for _index in range(0, _size)]
