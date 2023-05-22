from GroupAnagrams import Solution

from tests.base_tests import BaseUnitTest


class TestGroupAnagramsSolution(BaseUnitTest):

    def test_case_1(self):
        # Arrange
        # Act
        sut = Solution().groupAnagrams(
            strs=["eat", "tea", "tan", "ate", "nat", "bat"])
        # Assert
        assert sut is not None
        assert sut == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    def test_case_2(self):
        # Arrange
        # Act
        sut = Solution().groupAnagrams(strs=[""])
        # Assert
        assert sut is not None
        assert sut == [[""]]


    def test_case_3(self):
        # Arrange
        # Act
        sut = Solution().groupAnagrams(strs=["a"])
        # Assert
        assert sut is not None
        assert sut == [["a"]]