import os
import random
from snips_nlu import SnipsNLUEngine, load_resources
from snips_nlu.exceptions import LoadingError
from Voithos.CommandHandler import CommandHandler


class Voithos:
    unknown_cmd_responses = [
        "Sorry, I didn't recognize that command.",
        "Sorry, I'm not sure what you're asking for...",
        "Oops! I'm not sure how to answer that."
    ]
    error_msg = "Oops! it seems that something went wrong. "
    engine_path = os.path.join('Voithos', 'utilities', 'NLU')

    def __init__(self):
        self.cmd_handler = CommandHandler(self)

    def respond(self, request_dict):
        """
        Create a response to a user input through the CommandHandler
        :param request_dict: Dictionary of parameters associated with a user request, such as input_text, date, etc.
        :return : A string response from Voithos
        """
        try:
            self.nlu_engine = SnipsNLUEngine.from_path(
                self.engine_path, resources=load_resources("snips_nlu_en"))
        # If the NLU engine is missing (eg retraining)
        except LoadingError:
            return self.error_msg

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
                response = self.error_msg

        return response
