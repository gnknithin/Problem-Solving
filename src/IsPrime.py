class Solution:
    def isPrime(self, value: int) -> bool:
        _is_prime = True

        if value <= 1:

            _is_prime = False

        elif value > 1:

            _to_half = value//2
            _div_by = 2

            while (_div_by <= _to_half):

                if value % _div_by == 0:

                    _is_prime = False
                    break

                _div_by += 1

        return _is_prime
