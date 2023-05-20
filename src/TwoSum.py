from typing import List


class Solution:
    # https://leetcode.com/problems/two-sum/description/
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _output:List[int] = list()
        _input_size = len(nums)
        for i in range(_input_size):
            for j in range(i+1, _input_size):
                if (
                    nums[i]+nums[j] == target
                ):
                    _output.extend([i, j])
                    break
        return _output
