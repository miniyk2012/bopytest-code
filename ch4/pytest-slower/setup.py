"""Setup for pytest-nice plugin."""

from setuptools import setup

setup(
    name='pytest-slower',
    version='0.1.0',
    description='A pytest plugin to provide check duration',
    url='https://wherever/you/have/info/on/this/package',
    author='Thomas Young',
    author_email='your_email@somewhere.com',
    license='proprietary',
    py_modules=['pytest_slower'],
    install_requires=['pytest'],
    entry_points={'pytest11': ['slower = pytest_slower', ], },
)
