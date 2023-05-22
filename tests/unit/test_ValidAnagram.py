from ValidAnagram import Solution

from tests.base_tests import BaseUnitTest


class TestValidAnagramSolution(BaseUnitTest):

    def test_case_1(self):
        # Arrange
        # Act
        sut = Solution().isAnagram(s="anagram", t="nagaram")
        # Assert
        assert sut is not None
        assert sut is True


    def test_case_2(self):
        # Arrange
        # Act
        sut = Solution().isAnagram(s="rat", t="car")
        # Assert
        assert sut is not None
        assert sut is False


    def test_case_3(self):
        # Arrange
        # Act
        sut = Solution().isAnagram(s="aacc", t="ccac")
        # Assert
        assert sut is not None
        assert sut is False