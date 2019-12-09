import pytest


@pytest.fixture(scope='module')
def my_list():
    yield list(range(10))
    print('end my_list')


@pytest.fixture()
def my_dict():
    yield dict.fromkeys(range(3))
    print('end my_dict')


tasks = [1,2,3,4,5]
def task_id(task):
    return f'task{task}'

@pytest.fixture(params=tasks, ids=task_id, scope='module')
def task(request):
    return request.param

def test_list(my_list):
    assert list(range(10)) == my_list

def test_dict(my_dict):
    assert {key: None for key in range(3)} == my_dict

def test_list_dict(my_dict, my_list):
    assert list(range(10)) == my_list
    assert {key: None for key in range(3)} == my_dict

def test_task1(task):
    assert task <= 5

def test_task2(task):
    assert task >= 0