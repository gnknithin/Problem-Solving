from IsPrime import Solution

from tests.base_tests import BaseUnitTest


class TestIsPrime(BaseUnitTest):
    

    def test_case_false(self):
        # Arrange
        _false_cases = [1, 4, 6, 8, 10, 15, 16]
        # Act
        for _each in _false_cases:
            sut = Solution().isPrime(value=_each)
            # Assert
            assert sut is not None
            assert isinstance(sut, bool)
            assert sut is False

    def test_case_true(self):
        # Arrange
        _true_cases = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
            37, 41, 43, 47, 53, 59, 61, 67,
            71, 73, 79, 83, 89, 97
        ]
        # Act
        for _each in _true_cases:
            sut = Solution().isPrime(value=_each)
            # Assert
            assert sut is not None
            assert isinstance(sut, bool)
            assert sut is True
