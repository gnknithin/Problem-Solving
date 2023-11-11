from collections import defaultdict
from typing import Dict, List, Tuple


class Solution:
    # https://leetcode.com/problems/group-anagrams/description/
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _result: Dict[Tuple[int], List[str]] = defaultdict(list)
        for each_string in strs:
            _count = [0]*26
            for each_char in each_string:
                _count[ord(each_char)-ord("a")] += 1

            _result[tuple(_count)].append(each_string)
        return list(_result.values())