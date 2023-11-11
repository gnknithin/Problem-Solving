from typing import Dict, List


class Solution:
    # https://leetcode.com/problems/valid-parentheses/description/
    def isValid(self, s: str) -> bool:
        _stack: List[str] = list()
        _isValid = True
        # _closeTotOpen: Dict[str, str] = {
        #     "}": "{",
        #     "]": "[",
        #     ")": "("
        # }
        _closeTotOpen: Dict[str, str] = dict(
            [
                (")", "("), ("]", "["), ("}", "{")
            ]
        )
        for each in s:
            if each in _closeTotOpen:
                if _stack and _stack[-1] == _closeTotOpen[each]:
                    _stack.pop()
                else:
                    _isValid = False
                    break
            else:
                _stack.append(each)
        return _isValid if not _stack else False
