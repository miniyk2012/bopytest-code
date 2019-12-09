import pytest


@pytest.fixture()
def sample_test(testdir, pytestconfig):
    seconds = pytestconfig.getoption('seconds')
    testdir.makepyfile("""
        def test_sleep():
            assert 1 == 1

    """)
    return testdir


def test_slow_duration(sample_test):
    result = sample_test.runpytest()
    result.stdout.fnmatch_lines(
        ['*slower-0.1.0', ]
    )
    assert result.ret == 0
