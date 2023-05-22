from typing import Dict, List


class Solution:
    # https://leetcode.com/problems/top-k-frequent-elements/description/
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _counter: Dict[int,int] = dict()
        for each in nums:
            _counter[each] = 1 + _counter.get(each, 0)
        _freq:List[List[int]] = [[] for _ in range(len(nums)+1)]
        for _num, _count in _counter.items():
            _freq[_count].append(_num)
        _output: List[int] = list()
        for i in range(len(nums),0,-1):
            for n in _freq[i]:
                _output.append(n)
                if len(_output) == k:
                    return _output
        return _output