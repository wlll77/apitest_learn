import pytest


# 数组的形式
# @pytest.mark.parametrize("name, word", [["安琪拉", "火焰是我最喜欢的玩具"], ["黄州", "周日被我射熄火了"], ["鲁班", "上上下下"]])
# def test_parametrize_02(name, word):
#     print(f'{name}的台词是{word}')

# 元组的形式
# @pytest.mark.parametrize("name, word", [("安琪拉", "火焰是我最喜欢的玩具"), ("黄州", "周日被我射熄火了"), ("鲁班", "上上下下")])
# def test_parametrize_02(name, word):
#     print(f'{name}的台词是{word}')


# 字典的形式
@pytest.mark.parametrize("hero", [{"name": "安琪拉", "word": "火焰是我最喜欢的玩具"}, {"name": "黄忠", "word": "周日被我射熄火了"},
                                  {"name": "小乔", "word": "上上下下"}])
def test_parametrize_02(hero):
    print(hero["name"])
    print(hero["word"])
