from GenerateParentheses import Solution

from tests.base_tests import BaseUnitTest


class TestGenerateParenthesesSolution(BaseUnitTest):
    def test_case_1(self):
        # Arrange
        # Act
        sut = Solution().generateParenthesis(n=3)
        # Assert
        assert sut is not None
        assert sut == ["((()))","(()())","(())()","()(())","()()()"]

    def test_case_2(self):
        # Arrange
        # Act
        sut = Solution().generateParenthesis(n=1)
        # Assert
        assert sut is not None
        assert sut == ["()"]