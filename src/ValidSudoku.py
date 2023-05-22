from collections import defaultdict
from typing import Dict, List, Set, Tuple


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        _isValid = True
        _columns: Dict[int,Set[str]] = defaultdict(set)
        _rows: Dict[int, Set[str]] = defaultdict(set)
        _square: Dict[Tuple[int,int], Set[str]] = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    (
                        board[r][c] in _rows[r]
                    )
                    or(
                        board[r][c] in _columns[c]
                    )
                    or(
                        board[r][c] in _square[(r//3,c//3)]
                    )
                ):
                    _isValid = False
                    break
                _columns[c].add(board[r][c])
                _rows[r].add(board[r][c])
                _square[(r//3,c//3)].add(board[r][c])
            if not _isValid:
                break
        return _isValid
