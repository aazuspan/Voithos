import os
import unittest

TEST_DIR = os.path.join('tests')

loader = unittest.TestLoader()
suite = loader.discover(TEST_DIR)
runner = unittest.TextTestRunner()
runner.run(suite)
