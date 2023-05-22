from ProductOfArrayExceptSelf import Solution

from tests.base_tests import BaseUnitTest


class TestProductOfArrayExceptSelfSolution(BaseUnitTest):

    def test_case_1(self):
        # Arrange
        # Act
        sut = Solution().productExceptSelf(
            nums=[1, 2, 3, 4]
        )
        # Assert
        assert sut is not None
        assert sut == [24, 12, 8, 6]


    def test_case_2(self):
        # Arrange
        # Act
        sut = Solution().productExceptSelf(
            nums=[-1, 1, 0, -3, 3],
        )
        # Assert
        assert sut is not None
        assert sut == [0,0,9,0,0]