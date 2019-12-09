"""pytester is needed for testing plugins."""
pytest_plugins = 'pytester'


import time
def pytest_addoption(parser):
    parser.addoption("--seconds", action="store", default="0.1",
                    help="sleep time")
