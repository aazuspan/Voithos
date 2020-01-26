import random
from Voithos.commands.Command import Command


class FlipCoin(Command):
    """
    Voithos flips a coin
    """
    name = 'flipcoin'
    utterances = [
        'flip a coin',
        'toss a coin',
        'do a coin toss',
        'heads or tails?',
        'tails or heads?',
        'coin toss',
        'flip coin'
    ]
    help_description = 'Have Voithos flip a coin.'

    def respond(self):
        """
        Return a random coin flip result
        """
        return random.choice(['Heads', 'Tails'])
