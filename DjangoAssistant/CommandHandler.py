import importlib
import pkgutil
import logging
from DjangoAssistant.commands.Command import Command

logging.basicConfig(level='DEBUG')


def command(command_class):
    """
    Decorator that adds commands to the list of registered commands
    """
    def wrapper(*args, **kwargs):
        """
        Instantiate the class as usual if it is called
        """
        return command_class(*args, **kwargs)

    logging.debug(f'Registered {command_class.__name__}')
    CommandHandler.commands.append(command_class)
    return wrapper


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
        :return: String response from a command or 'not a valid command'
        """
        for cmd in self.cmds:
            cmd_obj = cmd(user_input)

            if cmd_obj.recognize():
                cmd_obj.respond()
                return

        # TODO: Warn the user if no command could be recognized
