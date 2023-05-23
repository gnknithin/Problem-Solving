from ValidParentheses import Solution

from tests.base_tests import BaseUnitTest


class TestValidParenthesesSolution(BaseUnitTest):

    def test_case_1(self):
        # Arrange
        # Act
        sut = Solution().isValid(
            s="()"
        )
        # Assert
        assert sut is not None
        assert sut is True


    def test_case_2(self):
        # Arrange
        # Act
        sut = Solution().isValid(
            s="()[]{}"
        )
        # Assert
        assert sut is not None
        assert sut is True


    def test_case_3(self):
        # Arrange
        # Act
        sut = Solution().isValid(
            s="(]"
        )
        # Assert
        assert sut is not None
        assert sut is False

    def test_case_4(self):
        # Arrange
        # Act
        sut = Solution().isValid(
            s="["
        )
        # Assert
        assert sut is not None
        assert sut is False