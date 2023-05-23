from EvaluateReversePolishNotation import Solution

from tests.base_tests import BaseUnitTest


class TestEvaluateReversePolishNotation(BaseUnitTest):
    def test_case_1(self):
        # Arrange
        # Act
        sut = Solution().evalRPN(tokens=["2", "1", "+", "3", "*"])
        # Assert
        assert sut is not None
        assert sut == 9

    def test_case_2(self):
        # Arrange
        # Act
        sut = Solution().evalRPN(tokens=["4", "13", "5", "/", "+"])
        # Assert
        assert sut is not None
        assert sut == 6

    def test_case_3(self):
        # Arrange
        # Act
        sut = Solution().evalRPN(
            tokens=[
                "10", "6", "9", "3", "+", "-11",
                "*", "/", "*", "17", "+", "5", "+"
            ]
        )
        # Assert
        assert sut is not None
        assert sut == 22
