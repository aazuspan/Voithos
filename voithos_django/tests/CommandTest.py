import unittest


class CommandTest(unittest.TestCase):
    """
    Test superclass for all commands
    """
    def setUp(self):
        print("Testing method: " + self._testMethodName)
