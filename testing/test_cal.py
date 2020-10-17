import pytest

from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        print("calculate started")
        self.calc = Calculator()

    def teardown_class(self):
        print("calculate ended")

    @pytest.mark.parametrize(
        'a,b,expect', [
            [100, 100, 200], [1, 3, 4], [0.1, 0.1, 0.2]
        ], ids=["case1", "case2", "case3"]
    )
    def test_add(self, a, b, expect):
        # calc = Calculator()
        print(a)
        print(b)
        print(expect)
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize(
        'c,d,expect1', [
            [100, 100, 10000], [1, 0, 0], [0.1, 0.1, 0.01]
        ], ids=["case11", "case21", "case31"]
    )
    def test_mul(self, c, d, expect1):
        # calc = Calculator()
        print(c)
        print(d)
        print(round(expect1, 2))
        result = self.calc.mul(c, d)
        assert round(result, 2) == expect1
