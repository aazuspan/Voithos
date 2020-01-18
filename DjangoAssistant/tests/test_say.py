import unittest
from Assistant import Assistant
from commands.Say import Say


class SayTest(unittest.TestCase):
    assistant = Assistant()

    def test_say_string(self):
        say_string = 'repeat this'
        Say(say_string, self.assistant).respond()
        self.assertTrue(self.assistant.last_said, say_string)


if __name__ == '__main__':
    unittest.main()