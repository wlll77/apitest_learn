import pytest


@pytest.mark.run(order=1)
def test_login():
    print('login...')


def test_pay():
    print('pay...')


@pytest.mark.run(order=2)
def test_search():
    print('search...')

@pytest.mark.run(order=3)
def test_order():
    print('order...')
