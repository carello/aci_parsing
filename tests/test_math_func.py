import math_func
import pytest


@pytest.fixture(scope='module')
def tools_lib():
    print('\n-------setup-----------')
    t = 3
    yield t
    print('\n-------teardown------')
    del t


@pytest.mark.parametrize('num1, num2, result',[(7, 3, 10), ('Hello', ' chet', 'Hello chet'), (10.3, 10.7, 21)])
def test_add(num1, num2, result):
    assert math_func.add(num1, num2) == result


def test_prod(tools_lib):
    print('\t--- BOO ---')
    y = tools_lib
    z = list()
    #assert math_func.product(7, y) == 21
    assert type(z) == list

