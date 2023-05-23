from LongestConsecutiveSequence import Solution

from tests.base_tests import BaseUnitTest


class TestLongestConsecutiveSequenceSolution(BaseUnitTest):

    def test_case_1(self):
        # Arrange
        # Act
        sut = Solution().longestConsecutive(nums=[100, 4, 200, 1, 3, 2])
        # Assert
        assert sut is not None
        assert sut == 4


    def test_case_2(self):
        # Arrange
        # Act
        sut = Solution().longestConsecutive(
            nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        )
        # Assert
        assert sut is not None
        assert sut == 9
