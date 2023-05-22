from EncodeAndDecodeString import Solution

from tests.base_tests import BaseUnitTest


class TestEncodeAndDecodeStringSolution(BaseUnitTest):

    def test_case_1(self):
        # Arrange
        case_1 = ["lint", "code", "love", "you"]
        # Act
        encode_sut = Solution().encode(values=case_1)
        # Assert
        assert encode_sut is not None
        assert encode_sut == "lint:;code:;love:;you"
        # Act
        decode_sut = Solution().decode(value=encode_sut)
        # Assert
        assert decode_sut is not None
        assert decode_sut == case_1



    def test_case_2(self):
        # Arrange
        case_2 = ["we", "say", ":", "yes"]
        # Act
        encode_sut = Solution().encode(values=case_2)
        # Assert
        assert encode_sut is not None
        assert encode_sut == "we:;say:;::;yes"
        # Act
        decode_sut = Solution().decode(value=encode_sut)
        # Assert
        assert decode_sut is not None
        assert decode_sut == case_2