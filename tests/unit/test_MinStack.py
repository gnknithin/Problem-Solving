from MinStack import CustomStack

from tests.base_tests import BaseUnitTest


class TestCustomStackSolution(BaseUnitTest):

    def test_case_1(self):
        # Arrange
        # Act
        sut = CustomStack()
        # Assert
        assert sut is not None
        # Act
        assert sut.push(-3) is None
        assert sut.push(0) is None
        assert sut.push(5) is None
        # Assert
        assert sut.getMin() == -3
        assert sut.top() == 5
        assert sut.pop() is None