import importlib
import pkgutil
from Voithos.commands.Command import Command


class CommandHandler:
    """
    The framework that accepts user input and forwards it to the correct command
    """
    COMMAND_DIR = 'Voithos\\commands'

    def __init__(self, voithos):
        self.voithos = voithos
        self.cmd_list = self.get_commands()

    def get_commands(self):
        """
        Find all commands in the command directory and import them. Then return all of them that are subclasses of
        Command in a list
        :return : A list of classes which are subclasses of Command
        """
        # TODO: Fix the import error that's causing commands to not load
        for (module_loader, name, ispkg) in pkgutil.iter_modules([self.COMMAND_DIR]):
            importlib.import_module('Voithos.commands.' + name, __package__)
        return Command.__subclasses__()

    def choose_command(self, request_dict):
        """
        Check all loaded commands to see if one recognizes the user input. If so, instantiate and return that command.
        :param request_dict: Dictionary of parameters associated with a user request, such as input_text, date, etc.
        :return: An instantiated command if one recognizes the input text, else None
        """
        for cmd in self.cmd_list:
            if cmd.recognize(request_dict['input_text']):
                return cmd(request_dict, self.voithos)
        return None
