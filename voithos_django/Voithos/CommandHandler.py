import importlib
import pkgutil
import os
from Voithos.commands.Command import Command


class CommandHandler:
    """
    The framework that accepts user input and forwards it to the correct command
    """
    COMMAND_DIR = os.path.join('voithos_django', 'Voithos', 'commands')

    def __init__(self, voithos):
        self.voithos = voithos
        self.cmd_list = self.get_commands()

    def get_commands(self):
        """
        Find all commands in the command directory and import them. Then return all of them that are subclasses of
        Command in a list
        :return : A list of classes which are subclasses of Command
        """
        for (module_loader, name, ispkg) in pkgutil.iter_modules([self.COMMAND_DIR]):
            importlib.import_module('Voithos.commands.' + name, __package__)
        return Command.__subclasses__()

    def choose_command(self, request_dict):
        """
        Find the best matching command to respond to a request dictionary
        :param request_dict: Dictionary of parameters associated with a user request, such as input_text, date, etc.
        :return: An instantiated command if one recognizes the input text, else None
        """
        cmd = None
        cmd_name = self.parse_cmd_name(request_dict['input_text'])
        if cmd_name:
            cmd = self.get_cmd_from_name(cmd_name)
        if cmd:
            cmd = cmd(request_dict=request_dict, voithos=self.voithos)
        return cmd

    def parse_cmd_name(self, user_input):
        """
        Use the Voithos NLU engine identify a command name from a user input
        :param user_input: User submitted string that may contain a command
        :return: The name of a command if one is recognized, or else None
        """
        result = self.voithos.nlu_engine.parse(user_input)
        return result['intent']['intentName']

    def get_cmd_from_name(self, cmd_name):
        """
        Find the command class that matches a given command name
        :param cmd_name: String name of a command
        :return: A command class
        """
        for cmd in self.cmd_list:
            if cmd.name == cmd_name:
                return cmd
