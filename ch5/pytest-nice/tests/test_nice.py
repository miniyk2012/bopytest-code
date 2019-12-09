"""Testing the pytest-nice plugin."""

import pytest


def test_pass_fail(testdir):

    # create a temporary pytest test module
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1

        def test_fail():
            assert 1 == 2
    """)

    # run pytest
    result = testdir.runpytest()

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*.F*',  # . for Pass, F for Fail
    ])

    # make sure that that we get a '1' exit code for the testsuite
    """
    Possible exit codes
    Running pytest can result in six different exit codes:

    Exit code 0:	All tests were collected and passed successfully
    Exit code 1:	Tests were collected and run but some of the tests failed
    Exit code 2:	Test execution was interrupted by the user
    Exit code 3:	Internal error happened while executing tests
    Exit code 4:	pytest command line usage error
    Exit code 5:	No tests were collected
    """

    assert result.ret == 1


@pytest.fixture()
def sample_test(testdir):
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1

        def test_fail():
            assert 1 == 2
    """)
    return testdir

def test_with_ini_nice(sample_test):
    sample_test.makefile('.ini', pytest="""
    [pytest]
    nice = True
    """)
    result = sample_test.runpytest()
    result.stdout.fnmatch_lines(['*.O*', ])  # . for Pass, O for Fail
    assert result.ret == 1

def test_with_ini_nice_verbose(sample_test):
    sample_test.makefile('.ini', pytest="""
    [pytest]
    nice = True
    """)
    result = sample_test.runpytest('-v')
    result.stdout.fnmatch_lines([
        '*improvement ini*',
    ])
    assert result.ret == 1

def test_header_ini(sample_test):
    sample_test.makefile('.ini', pytest="""
    [pytest]
    nice = True
    """)
    result = sample_test.runpytest()
    result.stdout.fnmatch_lines(['Thanks for running the tests.[ini]'])


def test_with_nice(sample_test):
    result = sample_test.runpytest('--nice')
    result.stdout.fnmatch_lines(['*.O*', ])  # . for Pass, O for Fail
    assert result.ret == 1


def test_with_nice_verbose(sample_test):
    result = sample_test.runpytest('-v', '--nice')
    result.stdout.fnmatch_lines([
        '*::test_fail OPPORTUNITY for improvement*',
    ])
    assert result.ret == 1


def test_not_nice_verbose(sample_test):
    result = sample_test.runpytest('-v')
    result.stdout.fnmatch_lines(['*::test_fail FAILED*'])
    assert result.ret == 1


def test_header(sample_test):
    result = sample_test.runpytest('--nice')
    result.stdout.fnmatch_lines(['Thanks for running the tests.'])


def test_header_not_nice(sample_test):
    result = sample_test.runpytest()
    thanks_message = 'Thanks for running the tests.'
    assert thanks_message not in result.stdout.str()


def test_help_message(testdir):
    result = testdir.runpytest('--help')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        'nice:',
        '*--nice*nice: turn FAILED into OPPORTUNITY for improvement',
        '*nice (bool):          Turn failures into opportunities.'
    ])
