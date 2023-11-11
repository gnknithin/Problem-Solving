from TwoSum import Solution, AnotherSolution

from tests.base_tests import BaseUnitTest


class TestTwoSumSolution(BaseUnitTest):

    def test_case_1(self):
        # Arrange
        # Act
        sut = Solution().twoSum(
            nums=[2, 7, 11, 15],
            target=9
        )
        # Assert
        assert sut is not None
        assert sut == [0,1]


    def test_case_2(self):
        # Arrange
        # Act
        sut = Solution().twoSum(
            nums=[3, 2, 4],
            target=6
        )
        # Assert
        assert sut is not None
        assert sut == [1,2]


    def test_case_3(self):
        # Arrange
        # Act
        sut = Solution().twoSum(
            nums=[3, 3],
            target=6
        )
        # Assert
        assert sut is not None
        assert sut == [0,1]

class TestTwoSumAnotherSolution(BaseUnitTest):

    def test_case_1(self):
        # Arrange
        # Act
        sut = AnotherSolution().twoSum(
            nums=[2, 7, 11, 15],
            target=9
        )
        # Assert
        assert sut is not None
        assert sut == [0,1]


    def test_case_2(self):
        # Arrange
        # Act
        sut = AnotherSolution().twoSum(
            nums=[3, 2, 4],
            target=6
        )
        # Assert
        assert sut is not None
        assert sut == [1,2]


    def test_case_3(self):
        # Arrange
        # Act
        sut = AnotherSolution().twoSum(
            nums=[3, 3],
            target=6
        )
        # Assert
        assert sut is not None
        assert sut == [0,1]