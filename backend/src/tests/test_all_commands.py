from tests.CommandTest import CommandTest
from Voithos.Voithos import Voithos


class AllCommandsTest(CommandTest):
    """
    This class handles tests that are run for every Voithos command
    """
    voithos = Voithos()

    def test_no_duplicate_names(self):
        """
        Test that there are no duplicate names between commands that would cause issues for the NLU engine
        """
        cmd_names = []
        for cmd in self.voithos.cmd_handler.cmd_list:
            self.assertTrue(cmd.name not in cmd_names)
            cmd_names.append(cmd.name)
