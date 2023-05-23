class CustomStack:

    def __init__(self):
        self._storage = list()

    def push(self, val: int) -> None:
        self._storage.append(val)

    def pop(self) -> None:
        self._storage.pop()

    def top(self) -> int:
        return self._storage[-1]

    def getMin(self) -> int:
        return min(self._storage)
