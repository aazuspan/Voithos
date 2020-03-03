from Voithos.commands.Command import Command


class Time(Command):
    """
    Have Voithos give the current local user date and time
    """
    name = 'time'
    utterances = [
        'what time is it?',
        'what is the date?',
        'time',
        'date',
        "what's the date?",
    ]
    help_description = 'Have Voithos tell you the date and time.'

    def respond(self):
        return self.date
