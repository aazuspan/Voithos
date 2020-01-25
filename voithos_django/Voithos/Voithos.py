from Voithos.CommandHandler import CommandHandler


class Voithos:
    _prompt = "How can I help you?\n"

    def __init__(self):
        self.cmd_handler = CommandHandler(self)
        self.last_said = None

    def respond(self, request_dict):
        """
        Create a response to a user input through the CommandHandler
        :param request_dict: Dictionary of parameters associated with a user request, such as input_text, date, etc.
        :return : A string response from Voithos
        """
        responding_cmd = self.cmd_handler.choose_command(request_dict)
        if not responding_cmd:
            response = "Sorry, I didn't recognize that command."
        else:
            try:
                response = responding_cmd.respond()
            except Exception:
                pass
            if not response:
                response = "Sorry, it seems that something went wrong."

        self.last_said = response
        return response

    def prompt(self):
        """
        Return a basic prompt for the user
        :return: String prompt
        """
        return self._prompt
