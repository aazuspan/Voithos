import random
from Voithos.CommandHandler import CommandHandler


class Voithos:
    unknown_cmd_responses = [
        "Sorry, I didn't recognize that command.",
        "Sorry, I'm not sure what you're asking for...",
        "Oops! I'm not sure how to answer that."
    ]
    
    def __init__(self):
        self.cmd_handler = CommandHandler(self)

    def respond(self, request_dict):
        """
        Create a response to a user input through the CommandHandler
        :param request_dict: Dictionary of parameters associated with a user request, such as input_text, date, etc.
        :return : A string response from Voithos
        """
        responding_cmd = self.cmd_handler.choose_command(request_dict)
        response = None
        if not responding_cmd:
            response = random.choice(self.unknown_cmd_responses)
        else:
            try:
                response = responding_cmd.respond()
            except Exception:
                pass
            if not response:
                response = "Oops! it seems that something went wrong. "

        return response
