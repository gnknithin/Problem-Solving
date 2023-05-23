from collections import defaultdict
from typing import Dict, List, Tuple


class Solution:
    # https://leetcode.com/problems/group-anagrams/description/
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _res : Dict[Tuple[int,...],List[str]] = defaultdict(list)
        for s in strs:
            _count: List[int] = [0]*26
            for c in s:
                _count[ord(c)-ord("a")] +=1
            
            _res[tuple(_count)].append(s)
        
        return list(_res.values())