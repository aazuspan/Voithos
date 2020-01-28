import random
from Voithos.commands.Command import Command


class Greeting(Command):
    """
    Respond to a greeting
    """
    name = 'greeting'
    utterances = [
        'hello',
        'hi',
        'hello Voithos',
        'hi Voithos',
        "What's up Voithos?",
        'greetings',
        'howdy',
        'hey',
        'hey voithos',
    ]
    help_description = 'Voithos responds to a greeting.'
    response_list = [
        'Hello!',
        'Hi!',
        'Hi there',
    ]

    def respond(self):
        response = random.choice(self.response_list)

        return response
