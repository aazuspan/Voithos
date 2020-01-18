import os
import unittest

loader = unittest.TestLoader()
TEST_DIR = os.path.join('Voithos', 'tests')
suite = loader.discover(TEST_DIR)
runner = unittest.TextTestRunner()
runner.run(suite)