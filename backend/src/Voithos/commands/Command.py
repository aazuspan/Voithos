from abc import abstractmethod
from Voithos.utilities.require_attributes import require_attributes


class Command(metaclass=require_attributes("name", "utterances", "help_description")):
    """
    A recognized command accepted by the voithos with a defined response.

    recognized_keywords and help_description must be implemented in all subclasses.
    """
    name = None
    utterances = None
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

    @abstractmethod
    def respond(self):
        return

    @classmethod
    def help(cls):
        """
        Print the name of the command and the help description for it
        """
        return f'<b>{cls.name}</b>: {cls.help_description}'
