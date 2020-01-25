from Voithos.CommandHandler import CommandHandler


class Voithos:
    def __init__(self):
        self.cmd_handler = CommandHandler(self)

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

        return response
