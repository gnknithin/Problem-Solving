from typing import Any, Dict


class Solution:
    # https://leetcode.com/problems/valid-anagram/description
    def isAnagram(self, s: str, t: str) -> bool:
        _isAnagram = False
        if len(s) == len(t):
            counter_s: Dict[Any, Any]=dict()
            counter_t: Dict[Any, Any] = dict()
            for each in range(len(s)):
                counter_s[s[each]] = 1 + counter_s.get(s[each], 0)
                counter_t[t[each]] = 1 + counter_t.get(t[each], 0)

            for _char in counter_s:
                if counter_s[_char] != counter_t.get(_char, 0):
                    _isAnagram = False
                    break
            else:
                _isAnagram = True
        return _isAnagram