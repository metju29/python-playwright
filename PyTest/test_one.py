import pytest


@pytest.mark.important_test
def test_failing():
    assert (1, 2, 3) == (3, 2, 1)
