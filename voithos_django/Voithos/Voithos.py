from Voithos.CommandHandler import CommandHandler


class Voithos:
    _prompt = "How can I help you?\n"

    def __init__(self):
        self.cmd_handler = CommandHandler(self)
        self.last_said = None

    def respond(self, user_input):
        """
        Create a response to a user input through the CommandHandler
        :param user_input: String input from user
        :return : A string response from Voithos
        """
        response = self.cmd_handler.respond(user_input)
        if not response:
            response = "Sorry, I didn't recognize that command."

        self.last_said = response
        return response

    def prompt(self):
        """
        Return a basic prompt for the user
        :return: String prompt
        """
        return self._prompt
