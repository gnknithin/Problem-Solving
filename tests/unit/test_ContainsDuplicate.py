from ContainsDuplicate import Solution

from tests.base_tests import BaseUnitTest


class TestContainsDuplicateSolution(BaseUnitTest):

    def test_case_1(self):
        # Arrange
        # Act
        sut = Solution().containsDuplicate(nums=[1, 2, 3, 1])
        # Assert
        assert sut is not None
        assert isinstance(sut,bool)
        assert sut is True


    def test_case_2(self):
        # Arrange
        # Act
        sut = Solution().containsDuplicate(nums=[1, 2, 3, 4])
        # Assert
        assert sut is not None
        assert isinstance(sut, bool)
        assert sut is False

    def test_case_3(self):
        # Arrange
        # Act
        sut = Solution().containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2])
        # Assert
        assert sut is not None
        assert isinstance(sut, bool)
        assert sut is True
