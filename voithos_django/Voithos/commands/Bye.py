from Voithos.commands.Command import Command


class Bye(Command):
    """
    Close Voithos
    """
    recognized_keywords = ['bye', 'goodbye', 'close', 'exit']
    help_description = 'Close Voithos.'

    def respond(self):
        """
        Say goodbye
        """
        return 'Goodbye'
