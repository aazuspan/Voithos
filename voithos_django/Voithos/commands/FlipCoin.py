import random
from Voithos.commands.Command import Command


class FlipCoin(Command):
    """
    Voithos flips a coin
    """
    recognized_keywords = ['flip a coin']
    help_description = 'Have Voithos flip a coin.'

    def respond(self):
        """
        Return a random coin flip result
        """
        return random.choice(['Heads', 'Tails'])
