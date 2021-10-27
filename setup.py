from setuptools import find_packages, setup

setup(
    name='pyleetcode',
    packages=find_packages(include=['pyleetcode']),
    version='0.0.1',
    description='Contains functions that solves leetcode questions',
    author='Festus Murimi',
    license='MIT',
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)