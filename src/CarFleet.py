from typing import List


class Solution:
    # https://leetcode.com/problems/car-fleet/description/
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        _pairs : List[List[int]] = [[p,s] for p,s in zip(position,speed)]
        _stack: List[float] = list()
        for p,s in sorted(_pairs)[::-1]: # Reverse Sorted Order
            _stack.append((target-p)/s)
            if len(_stack) >=2 and _stack[-1] <= _stack[-2]:
                _stack.pop()
        return len(_stack)
