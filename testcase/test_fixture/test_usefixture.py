import pytest


@pytest.mark.usefixtures("use_fixture1", "use_fixture2")
def test_usefixture():

    print("usefixtures")
