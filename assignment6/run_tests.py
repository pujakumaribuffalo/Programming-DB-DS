import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner
import os

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')
    if os.path.exists('/autograder/results/'):
        filepath = '/autograder/results/results.json'
    else:
        filepath = './results.json'

    with open(filepath, 'w') as f:
        JSONTestRunner(visibility='visible', stream=f).run(suite)
