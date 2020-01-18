from abc import abstractmethod, ABCMeta


class Command(metaclass=ABCMeta):
    """
    A recognized command accepted by the Assistant with a defined response
    """
    recognized_commands = None

    def __init__(self, user_input):
        self.user_input = user_input

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
