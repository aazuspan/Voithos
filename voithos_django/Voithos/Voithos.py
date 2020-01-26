import os
import random
from snips_nlu import SnipsNLUEngine
from Voithos.CommandHandler import CommandHandler


class Voithos:
    unknown_cmd_responses = [
        "Sorry, I didn't recognize that command.",
        "Sorry, I'm not sure what you're asking for...",
        "Oops! I'm not sure how to answer that."
    ]
    engine_path = os.path.join('Voithos', 'utilities', 'NLU')
    
    def __init__(self):
        self.cmd_handler = CommandHandler(self)
        self.nlu_engine = SnipsNLUEngine.from_path(self.engine_path)

    def respond(self, request_dict):
        """
        Create a response to a user input through the CommandHandler
        :param request_dict: Dictionary of parameters associated with a user request, such as input_text, date, etc.
        :return : A string response from Voithos
        """
        cmd = self.cmd_handler.choose_command(request_dict)

        response = None
        if not cmd:
            response = random.choice(self.unknown_cmd_responses)
        else:
            try:
                response = cmd.respond()
            except Exception:
                pass
            if not response:
                response = "Oops! it seems that something went wrong. "

        return response
