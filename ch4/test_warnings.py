import warnings
import pytest


def lame_function(message="Please stop using this"):
    warnings.warn(message, DeprecationWarning)
    # rest of function


def test_lame_function(recwarn):
    message = "hahah"
    lame_function(message+'x')
    lame_function(message)
    assert len(recwarn) == 2
    w = recwarn.pop()
    assert w.category == DeprecationWarning
    print('warning', w)
    print('message', w.message)
    print('category', w.category)
    assert str(w.message) == message+'x'
    w = recwarn.pop()
    assert str(w.message) == message


def test_lame_function_2():
    with pytest.warns(None) as warning_list:
        lame_function()

    assert len(warning_list) == 1
    w = warning_list.pop()
    assert w.category == DeprecationWarning
    assert str(w.message) == 'Please stop using this'


lame_function()
