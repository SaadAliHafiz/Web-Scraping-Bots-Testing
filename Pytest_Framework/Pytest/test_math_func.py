import math
from math_func import StudentDB
import pytest
db=None
def setup_module(module):
    global db
    print("----------------setup----------------")
    db=StudentDB()
    db.connect('C:/Users/Saad/OneDrive/Desktop/Python/Pytest/data.json')

def teardown_module(module):
    print("----------------Teardown----------------")
#     db.close()
def test_scott_data():
    # db=StudentDB()
    # db.connect('C:/Users/Saad/OneDrive/Desktop/Python/Pytest/data.json')
    scott_data=db.get_data('Scott')
    assert scott_data['id']==1
    assert scott_data['name']=='Scott'
    assert scott_data['result']=='pass'
    
def test_mark_data():
    # db=StudentDB()
    # db.connect('C:/Users/Saad/OneDrive/Desktop/Python/Pytest/data.json')
    mark_data=db.get_data('Mark')
    assert mark_data['id']==2
    assert mark_data['name']=='Mark'
    assert mark_data['result']=='fail'




























# @pytest.mark.parametrize('num1,num2,result',
#     [
#         (7,3,10),
#         (7,2,9),
#         (5,2,7)
#     ]
# )

# def test_add(num1,num2,result):
#     assert math_func.add(num1,num2)==result

# def test_add():
#     assert math_func.add(7,3)==10
#     assert math_func.add(7)==9
#     assert math_func.add(5)==7
#     print(math_func.add(5),"------------")

# def test_product():
#     assert math_func.product(5,5)==25
#     assert math_func.product(5,6) ==30
    
    


# def test_add_str():
#     result=math_func.add("Hello ","there")
#     assert result =="Hello there"
#     assert type(result) is str
#     assert 'Helso' not in result



# def test_product_str():
#     assert math_func.product("Hello ",3)=="Hello Hello Hello "
#     result=math_func.product("hello ")
#     assert result=="hello hello "
#     assert type(result) is str
#     assert "hello" in result