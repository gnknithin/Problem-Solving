from typing import List


class Solution:
    # https://leetcode.com/problems/longest-consecutive-sequence/description/
    def longestConsecutive(self, nums: List[int]) -> int:
        _longest = 0
        _numSet = set(nums)
        for n in nums:
            # Check if it is the start of sequence
            if (n-1) not in _numSet:
                _length = 0
                while (n+_length in _numSet):
                    _length +=1
                _longest = max(_length,_longest)
        return _longest
