from Voithos.commands.Command import Command


class Bye(Command):
    """
    Close Voithos
    """
    recognized_commands = ['bye', 'goodbye', 'close', 'exit']
    help_description = 'Close Voithos.'

    def respond(self):
        """
        Say goodbye
        """
        self.voithos.say('Goodbye')
        self.voithos.kill()
