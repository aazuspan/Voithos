import importlib
import pkgutil
from DjangoAssistant.commands.Command import Command


class CommandHandler:
    """
    The framework that accepts user input and forward it to the correct command
    """
    COMMAND_DIR = 'commands'

    def __init__(self):
        self.cmds = self.load_commands()

    def load_commands(self):
        """
        Find all commands in the command directory and import them. Then return all of them that are subclasses of
        Command
        :return : A list of classes which are subclasses of Command
        """
        for (module_loader, name, ispkg) in pkgutil.iter_modules([self.COMMAND_DIR]):
            importlib.import_module('DjangoAssistant.commands.' + name, __package__)
        return Command.__subclasses__()

    def respond(self, user_input):
        """
        Check all loaded commands to see if one recognizes the user input. If so, have that command handle the response.
        :param user_input:
        :return: True if command was handled, false if no commands were recognized
        """
        for cmd in self.cmds:
            cmd_obj = cmd(user_input)

            if cmd_obj.recognize():
                cmd_obj.respond()
                return True
        return False
