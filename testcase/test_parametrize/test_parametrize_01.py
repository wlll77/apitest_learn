import pytest

# 单参数 单次循环
# @pytest.mark.parametrize("name", ["老白"])
# def test_parameteize(name):
#     print("我是"+ name)


# 单参数 多次循环
# 运行时，将数组里的值分别赋值给变量，每赋值一次，运行一次
@pytest.mark.parametrize("name", ["老白", "小粉", "大乔"])
def test_parameteize(name):
    assert name == "老白"
