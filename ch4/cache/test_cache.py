
import pytest

@pytest.fixture()
def key():
    return 'cache/test_cache'


def test_before(cache, key):
    cache.set(key, 'value')

def test_after(cache, key):
    print(cache.get(key, None))