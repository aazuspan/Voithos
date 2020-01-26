from Voithos.commands.Command import Command


class Bye(Command):
    """
    Close Voithos
    """
    name = 'bye'
    utterances = [
        'bye',
        'goodbye',
        'see you later',
        'bye Voithos',
        'goodbye Voithos',
        "I'm leaving"
    ]
    help_description = 'Close Voithos.'

    def respond(self):
        """
        Say goodbye
        """
        return 'Goodbye'
