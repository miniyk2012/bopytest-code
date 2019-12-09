"""Code for pytest-nice plugin."""

import pytest


def pytest_addoption(parser):
    """Turn nice features on with --nice option."""
    group = parser.getgroup('nice')
    group.addoption("--nice", action="store_true",
                    help="nice: turn FAILED into OPPORTUNITY for improvement")
    parser.addini('nice', type='bool', help='Turn failures into opportunities.')


def pytest_report_header(config):
    """Thank tester for running tests."""
    if config.getoption('nice'):
        return "Thanks for running the tests."
    if config.getini('nice'):
        return "Thanks for running the tests.[ini]"


def pytest_report_teststatus(report, config):
    """Turn failures into opportunities."""
    if report.when == 'call':
        if report.failed and config.getoption('nice'):
            return (report.outcome, 'O', 'OPPORTUNITY for improvement')
        if report.failed and config.getini('nice'):
            return (report.outcome, 'O', 'OPPORTUNITY for improvement ini')