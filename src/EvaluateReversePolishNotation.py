from typing import List


class Solution:
    # https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
    def evalRPN(self, tokens: List[str]) -> int:
        _result : List[int] = list()
        for each in tokens:
            if each == "+":
                _result.append(_result.pop()+_result.pop())
            elif each == "-":
                a,b = _result.pop(),_result.pop()
                _result.append(b-a)
            elif each == "*":
                _result.append(_result.pop()*_result.pop())
            elif each == "/":
                a,b = _result.pop(),_result.pop()
                _result.append(int(b/a))
            else:
                _result.append(int(each))
        return _result[0]