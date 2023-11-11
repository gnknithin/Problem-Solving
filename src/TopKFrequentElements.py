from collections import defaultdict
from typing import Dict, List


class Solution:
    # https://leetcode.com/problems/top-k-frequent-elements/description/
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _freq_counter: Dict[int, int] = defaultdict(int)
        _freq: Dict[int, List[int]] = defaultdict(list)
        _top_k_freq: List[int] = list()
        for each in nums:
            _freq_counter[each] += 1
        for _each_num, _num_count in _freq_counter.items():
            _freq[_num_count].append(_each_num)
        for each in range(len(nums), 0, -1):
            if (each in _freq) and (len(_freq[each]) > 0):
                _top_k_freq.extend(_freq[each])
            if len(_top_k_freq) == k:
                break
        return _top_k_freq
