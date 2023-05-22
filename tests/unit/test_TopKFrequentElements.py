from TopKFrequentElements import Solution

from tests.base_tests import BaseUnitTest


class TestTopKFrequentElementsSolution(BaseUnitTest):

    def test_case_1(self):
        # Arrange
        # Act
        sut = Solution().topKFrequent(
            nums=[1, 1, 1, 2, 2, 3],
            k=2
        )
        # Assert
        assert sut is not None
        assert sut == [1, 2]

    def test_case_2(self):
        # Arrange
        # Act
        sut = Solution().topKFrequent(
            nums=[1],
            k=1
        )
        # Assert
        assert sut is not None
        assert sut == [1]

    def test_case_3(self):
        # Arrange
        # Act
        sut = Solution().topKFrequent(
            nums=[1,2],
            k=2
        )
        # Assert
        assert sut is not None
        assert sut == [1,2]