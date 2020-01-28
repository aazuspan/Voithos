import requests
from Voithos.commands.Command import Command


class RandomFact(Command):
    """
    Return a random fact
    """
    name = 'random fact'
    utterances = [
        'tell me a random fact',
        'random fact',
        'fact',
        'give me a random fact',
        'tell me a fact, Voithos',
    ]
    help_description = 'Have Voithos tell you a random fact.'

    def respond(self):
        url = 'https://uselessfacts.jsph.pl/random.json?language=en'
        response = requests.get(url).json()
        fact = response['text']

        return fact
