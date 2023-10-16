import pytest

@pytest.mark.pro
class TestThree:


    def test_one(self):
        expect = 1
        actual = 1
        assert expect == actual



    def test_two(self):
        expect = 1
        actual = 2
        assert expect == actual


    def three(self):  # 测试用例方法不用 test_ 开头的话，不会被执行
        expect = 1
        actual = 1
        assert expect == actual
