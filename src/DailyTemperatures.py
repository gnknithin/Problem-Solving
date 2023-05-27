from typing import List


class Solution:
    # https://leetcode.com/problems/daily-temperatures/description/
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        _answer : List[int] = [0]*len(temperatures)
        _stack : List[List[int]] = list() # Pair [temperature,index]
        for _index,_temp in enumerate(temperatures):
            while _stack and _temp > _stack[-1][0]:
                _stackTemp, _stackIndex = _stack.pop()
                _answer[_stackIndex] = _index-_stackIndex
            _stack.append([_temp,_index])
        return _answer
