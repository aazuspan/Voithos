import os
import sys
import unittest

TEST_DIR = os.path.join('tests')
sys.path.insert(0, os.path.join('voithos_django'))

loader = unittest.TestLoader()
suite = loader.discover(TEST_DIR)
runner = unittest.TextTestRunner()
runner.run(suite)
