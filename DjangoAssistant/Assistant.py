from CommandHandler import CommandHandler


class Assistant:
    _prompt = "How can I help you?\n"

    def __init__(self):
        self.cmd_handler = CommandHandler()

    def respond(self, user_input):
        """
        Create a response to a user input
        :param user_input: String input from user
        :return: String response from Assistant
        """
        response = self.cmd_handler.respond(user_input)
        self.say(response)

    def prompt(self):
        """
        Return a basic prompt for the user
        :return: String prompt
        """
        return self._prompt

    def parse_input(self, user_input):
        """

        :param user_input: String input from user
        :return:
        """
        pass

    @staticmethod
    def say(to_say):
        print(to_say)