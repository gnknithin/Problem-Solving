from DailyTemperatures import Solution

from tests.base_tests import BaseUnitTest


class TestDailyTemperaturesSolution(BaseUnitTest):

    def test_case_1(self):
        # Arrange
        # Act
        sut = Solution().dailyTemperatures(
            temperatures=[73, 74, 75, 71, 69, 72, 76, 73],
        )
        # Assert
        assert sut is not None
        assert sut == [1, 1, 4, 2, 1, 1, 0, 0]


    def test_case_2(self):
        # Arrange
        # Act
        sut = Solution().dailyTemperatures(
            temperatures=[30, 40, 50, 60],
        )
        # Assert
        assert sut is not None
        assert sut == [1, 1, 1, 0]


    def test_case_3(self):
        # Arrange
        # Act
        sut = Solution().dailyTemperatures(
            temperatures=[30, 60, 90],
        )
        # Assert
        assert sut is not None
        assert sut == [1, 1, 0]
