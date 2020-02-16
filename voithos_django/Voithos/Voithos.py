import logging
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
    engine_path = os.path.join('voithos_django', 'Voithos', 'utilities', 'NLU')
    logging.basicConfig(level=logging.INFO)

    def __init__(self):
        self.cmd_handler = CommandHandler(self)

    def respond(self, request_dict):
        """
        Create a response to a user input through the CommandHandler
        :param request_dict: Dictionary of parameters associated with a user request, such as input_text, date, etc.
        :return : A string response from Voithos and the delay for posting that response in millis
        """
        response = None
        response_delay = 0

        self.nlu_engine = self.load_nlu_engine()
        if not self.nlu_engine:
            response = self.error_msg

        cmd = self.cmd_handler.choose_command(request_dict)

        if not cmd:
            response = random.choice(self.unknown_cmd_responses)
        else:
            try:
                response = str(cmd.respond())
            except Exception:
                logging.exception('Error generating response!')
            if not response:
                response = self.error_msg

            if cmd.name != 'help':
                response_delay = self.calculate_response_delay()

            logging.info(
                f'Input "{request_dict["input_text"]}" generates response "{response}" from command "{cmd.name}"')
        return response, response_delay

    def load_nlu_engine(self):
        """
        Try to load the NLU engine from the local drive.
        :return : Trained SnipsNLUEngine or none
        """
        nlu_engine = None
        try:
            nlu_engine = SnipsNLUEngine.from_path(self.engine_path)
        except LoadingError:
            logging.exception('Failed to load NLU engine!')

        return nlu_engine

    @staticmethod
    def calculate_response_delay():
        """
        Calculate an appropriate delay time for Voithos to process a given response
        :return: Delay time in milliseconds
        """
        min_response_delay = 1000

        return min_response_delay
