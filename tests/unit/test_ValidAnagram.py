from ValidAnagram import AnotherSolution, AnotherSolutionWithDict, Solution

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


class TestValidAnagramAnotherSolutionWithDict(BaseUnitTest):

    def test_case_1(self):
        # Arrange
        # Act
        sut = AnotherSolutionWithDict().isAnagram(s="anagram", t="nagaram")
        # Assert
        assert sut is not None
        assert sut is True

    def test_case_2(self):
        # Arrange
        # Act
        sut = AnotherSolutionWithDict().isAnagram(s="rat", t="car")
        # Assert
        assert sut is not None
        assert sut is False

    def test_case_3(self):
        # Arrange
        # Act
        sut = AnotherSolutionWithDict().isAnagram(s="aacc", t="ccac")
        # Assert
        assert sut is not None
        assert sut is False


class TestValidAnagramAnotherSolution(BaseUnitTest):

    def test_case_1(self):
        # Arrange
        # Act
        sut = AnotherSolution().isAnagram(s="anagram", t="nagaram")
        # Assert
        assert sut is not None
        assert sut is True

    def test_case_2(self):
        # Arrange
        # Act
        sut = AnotherSolution().isAnagram(s="rat", t="car")
        # Assert
        assert sut is not None
        assert sut is False

    def test_case_3(self):
        # Arrange
        # Act
        sut = AnotherSolution().isAnagram(s="aacc", t="ccac")
        # Assert
        assert sut is not None
        assert sut is False
