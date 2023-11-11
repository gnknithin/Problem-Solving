from typing import Any, Dict, List


class Solution:
    # https://leetcode.com/problems/valid-anagram/description
    def isAnagram(self, s: str, t: str) -> bool:
        _isAnagram = False
        if len(s) == len(t):
            counter_s: Dict[Any, Any] = dict()
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


class AnotherSolutionWithDict:
    def isAnagram(self, s: str, t: str) -> bool:
        _isAnagram = False
        if len(s) == len(t):
            _size = len(s)
            i = 0
            _s_counter = dict()
            _t_counter = dict()
            while (i < _size):
                _s_counter[s[i]] = _s_counter.get(s[i], 0)+1
                _t_counter[t[i]] = _t_counter.get(t[i], 0)+1
                i += 1
            _isAnagram = _s_counter == _t_counter
        return _isAnagram




class AnotherSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        _isAnagram = False

        if len(s) == len(t):
            counter_s: List[int] = [0]*26
            counter_t: List[int] = [0]*26
            for each in range(len(s)):
                counter_s[ord(s[each])-97] += 1
                counter_t[ord(t[each])-97] += 1
            _isAnagram = bool(tuple(counter_s) == tuple(counter_t))
        return _isAnagram
