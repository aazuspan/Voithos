import importlib
import pkgutil
from Voithos.commands.Command import Command


class CommandHandler:
    """
    The framework that accepts user input and forwards it to the correct command
    """
    COMMAND_DIR = 'commands'

    def __init__(self, voithos):
        self.voithos = voithos
        self.cmd_list = self.get_commands()
        self.cmds = self.load_commands()

    def get_commands(self):
        """
        Find all commands in the command directory and import them. Then return all of them that are subclasses of
        Command in a list
        :return : A list of classes which are subclasses of Command
        """
        for (module_loader, name, ispkg) in pkgutil.iter_modules([self.COMMAND_DIR]):
            importlib.import_module('Voithos.commands.' + name, __package__)
        return Command.__subclasses__()

    def load_commands(self):
        """
        Instantiate all commands and store them for later use
        :return:
        """
        loaded_cmds = []
        for cmd in self.cmd_list:
            loaded_cmds.append(cmd(user_input=None, voithos=self.voithos))
        return loaded_cmds

    def respond(self, user_input):
        """
        Check all loaded commands to see if one recognizes the user input. If so, have that command handle the response.
        :param user_input:
        :return: True if command was handled, false if no commands were recognized
        """
        for cmd in self.cmds:
            cmd.user_input = user_input

            if cmd.recognize():
                cmd.respond()
                return True
        return False
