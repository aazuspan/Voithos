import logging
import os
import random
from snips_nlu import SnipsNLUEngine
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
    logging.basicConfig(level=logging.INFO)

    def __init__(self):
        self.cmd_handler = CommandHandler(self)

    def respond(self, request_dict):
        """
        Create a response to a user input through the CommandHandler
        :param request_dict: Dictionary of parameters associated with a user request, such as input_text, date, etc.
        :return : A string response from Voithos
        """
        try:
            self.nlu_engine = SnipsNLUEngine.from_path(self.engine_path)
        # If the NLU engine is missing (eg retraining)
        except LoadingError:
            logging.exception('Failed to load NLU engine!')
            return self.error_msg

        cmd = self.cmd_handler.choose_command(request_dict)
        response = None
        cmd_name = None
        if not cmd:
            response = random.choice(self.unknown_cmd_responses)
        else:
            cmd_name = cmd.name
            try:
                response = cmd.respond()
            except Exception:
                logging.exception('Error generating response!')
            if not response:
                response = self.error_msg

        logging.info(
            f'Input "{request_dict["input_text"]}" generates response "{response}" from command "{cmd_name}"')
        return response
