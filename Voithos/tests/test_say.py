import unittest
from Voithos.Voithos import Voithos
from commands.Say import Say


class SayTest(unittest.TestCase):
    voithos = Voithos()

    def test_say_string(self):
        say_string = 'repeat this'
        Say(say_string, self.voithos).respond()
        self.assertTrue(self.voithos.last_said, say_string)


if __name__ == '__main__':
    unittest.main()