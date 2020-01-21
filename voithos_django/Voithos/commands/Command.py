from abc import abstractmethod
from Voithos.utilities.require_attributes import require_attributes


class Command(metaclass=require_attributes("recognized_keywords", "help_description")):
    """
    A recognized command accepted by the voithos with a defined response.

    recognized_keywords and help_description must be implemented in all subclasses.
    """
    recognized_keywords = None
    help_description = None

    def __init__(self, user_input, voithos):
        self.user_input = user_input
        self.voithos = voithos

    def recognize(self):
        """
        Test if the user input is recognized as calling this command
        :param user_input: String input from user
        :return: True if recognized, False if not
        """
        for keyword in self.recognized_keywords:
            # TODO: Prevent partial matches (ie asdfbyefjdksl matches bye)
            if keyword in self.user_input.lower():
                return True
        return False

    @abstractmethod
    def respond(self):
        return

    def help(self):
        """
        Print the name of the command and the help description for it
        """
        return f'{self.recognized_keywords[0]}: {self.help_description}'
