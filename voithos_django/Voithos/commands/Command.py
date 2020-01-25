from abc import abstractmethod
from Voithos.utilities.require_attributes import require_attributes


class Command(metaclass=require_attributes("recognized_keywords", "help_description")):
    """
    A recognized command accepted by the voithos with a defined response.

    recognized_keywords and help_description must be implemented in all subclasses.
    """
    recognized_keywords = None
    help_description = None

    def __init__(self, request_dict, voithos):
        self.request_dict = request_dict
        self.voithos = voithos

    @property
    def user_input(self):
        return self.request_dict['input_text']

    @property
    def date(self):
        if self.request_dict['date']:
            return self.request_dict['date']
        else:
            return None

    @classmethod
    def recognize(cls, user_input):
        """
        Test if the user input is recognized as calling this command
        :param user_input: A string input by the user
        :return: True if recognized, False if not
        """
        for keyword in cls.recognized_keywords:
            # TODO: Prevent partial matches (ie asdfbyefjdksl matches bye)
            if keyword in user_input.lower():
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
