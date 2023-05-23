from typing import List


class Solution:
    # https://leetcode.com/problems/generate-parentheses/description/
    def generateParenthesis(self, n: int) -> List[str]:
        _stack: List[str] = list()
        _res: List[str] = list()
        def backtrack(openN:int,closedN:int):
            if (openN==closedN==n):
                _res.append(
                    "".join(_stack)
                )
                return
            
            if (openN < n):
                _stack.append("(")
                backtrack(openN=openN+1,closedN=closedN)
                _stack.pop()
            
            if (closedN < openN):
                _stack.append(")")
                backtrack(openN=openN,closedN=closedN+1)
                _stack.pop()
        
        backtrack(openN=0,closedN=0)
        return _res