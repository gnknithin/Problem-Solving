from CarFleet import Solution

from tests.base_tests import BaseUnitTest


class TestCarFleetSolution(BaseUnitTest):

    def test_case_1(self):
        # Arrange
        # Act
        sut = Solution().carFleet(
            target=12,
            position=[10, 8, 0, 5, 3],
            speed=[2, 4, 1, 1, 3]
        )
        # Assert
        assert sut is not None
        assert sut == 3


    def test_case_2(self):
        # Arrange
        # Act
        sut = Solution().carFleet(
            target=10,
            position=[3],
            speed=[3]
        )
        # Assert
        assert sut is not None
        assert sut == 1


    def test_case_3(self):
        # Arrange
        # Act
        sut = Solution().carFleet(
            target=100,
            position=[0, 2, 4],
            speed=[4,2,1]
        )
        # Assert
        assert sut is not None
        assert sut == 1
