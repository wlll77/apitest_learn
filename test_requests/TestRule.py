class TestRule:

    # 测试类中不能有init方法
    # def __init__(self):
    #     pass

    def test_rule(self):
        assert 1 == 2

    def test_rule2(self):
        assert 2 == 2