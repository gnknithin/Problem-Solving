from typing import List


class Solution:
    # https://www.lintcode.com/problem/659/
    def encode(self, values:List[str])->str:
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """
        # write your code here
        return ":;".join(values)

    def decode(self, value: str)->List[str]:
        """
        @param: str: A string
        @return: dcodes a single string to a list of strings
        """
        # write your code here
        return value.split(sep=":;")
