import requests
from Voithos.commands.Command import Command


class Joke(Command):
    """
    Return a joke
    """
    name = 'joke'
    utterances = [
        'tell me a joke',
        'joke',
        'give me a joke',
        'tell me a joke, Voithos',
    ]
    help_description = 'Have Voithos tell a random joke.'

    def respond(self):
        url = 'https://icanhazdadjoke.com/'
        headers = {'Accept': 'application/json'}
        response = requests.get(url, headers=headers).json()
        joke = response['joke']

        return joke
