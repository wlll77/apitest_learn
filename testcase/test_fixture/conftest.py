import pytest


@pytest.fixture(scope='session')   # 这里的参数也可以用autouse=True
def test_session():
    print("我是session级的fixture")

@pytest.fixture(scope="function")  # 这里的参数也可以用autouse=True
def test_func1():
    print("我是function1级的fixture")

@pytest.fixture(scope="function")
def test_func2():
    print("我是function2级的fixture")

@pytest.fixture(scope="function")
def get_params():
    params = {"shouji": "13456755448","appkey":"0c818521d38759e1"}
    return params

@pytest.fixture(scope="function")
def func():
    print("我是前置步骤33")
    yield
    print("我是后置步骤")

@pytest.fixture(scope="function")
def use_fixture1():
    print("我现在使用use_fixture1")
    return "fixture"

@pytest.fixture(scope="function")
def use_fixture2():
    print("我现在使用use_fixture2")