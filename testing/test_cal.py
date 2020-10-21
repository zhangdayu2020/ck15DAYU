import pytest
import yaml
from pythoncode.calculator import Calculator


def get_datas():
    with open( "./datas/calc.yml", encoding='utf-8' ) as f:
        datas = yaml.safe_load( f )
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    print( add_ids )
    print( add_datas )
    return [add_datas, add_ids]

class TestCalc:
    def setup_class(self):
        print("calculate started")
        self.calc = Calculator()

    def teardown_class(self):
        print("calculate ended")

    def setup(self):
        print("Case started")
        self.calc = Calculator()

    def teardown(self):
        print("Case ended")
    @pytest.mark.parametrize(
        'a,b,expect', get_datas()[0], ids=get_datas()[1]
    )
    def test_add(self, a, b, expect):
        # calc = Calculator()
        print(a)
        print(b)
        print(round(expect, 4))
        result = self.calc.add(a, b)
        assert round(result, 4) == round(expect, 4)

    @pytest.mark.parametrize(
        'c,d,expect1', [
            [100, 100, 10000], [1, 0, 0], [0.1, 0.1, 0.01], [-1, -1, 1], [-1, 2, -2], [0, 100, 0]
        ], ids=["case11", "case21", "case31", "case41", "case51", "case61", ]
    )
    def test_mul(self, c, d, expect1):
        # calc = Calculator()
        print(c)
        print(d)
        print(round(expect1, 4))
        result = self.calc.mul(c, d)
        assert round(result, 4) == round(expect1, 4)
