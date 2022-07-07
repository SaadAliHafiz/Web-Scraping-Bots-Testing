import math
import math_func
import pytest
# @pytest.mark.skip(reason="don't run the add test")

def test_add():
    assert math_func.add(7,3)==10
    assert math_func.add(7)==9
    assert math_func.add(5)==7
    print(math_func.add(5),"------------")

def test_product():
    assert math_func.product(5,5)==25
    assert math_func.product(5,6) ==30
    
    


def test_add_str():
    result=math_func.add("Hello ","there")
    assert result =="Hello there"
    assert type(result) is str
    assert 'Helso' not in result



def test_product_str():
    assert math_func.product("Hello ",3)=="Hello Hello Hello "
    result=math_func.product("hello ")
    assert result=="hello hello "
    assert type(result) is str
    assert "hello" in result
