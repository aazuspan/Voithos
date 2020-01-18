from abc import abstractmethod, ABCMeta
from utilities.require_attributes import require_attributes


class Command(metaclass=require_attributes("recognized_commands", "help_description")):
    """
    A recognized command accepted by the Assistant with a defined response.

    Recognized_commands and help_description must be implemented in all subclasses.
    """
    recognized_commands = None
    help_description = None

    def __init__(self, user_input, assistant):
        self.user_input = user_input
        self.assistant = assistant

    def recognize(self):
        """
        Test if the user input is recognized as calling this command
        :param user_input: String input from user
        :return: True if recognized, False if not
        """
        for command in self.recognized_commands:
            if self.user_input.lower().startswith(command):
                return True
        return False

    @abstractmethod
    def respond(self):
        return

    def help(self):
        """
        Print the name of the command and the help description for it
        """
        self.assistant.say(f'{self.recognized_commands[0]}: {self.help_description}')
