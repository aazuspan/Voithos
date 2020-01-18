from DjangoAssistant.commands.Command import Command


class Bye(Command):
    """
    Close the assistant
    """
    recognized_commands = ['bye', 'goodbye', 'close', 'exit']
    help_description = 'Close the assistant.'

    def respond(self):
        """
        Say goodbye
        """
        self.assistant.say('Goodbye')
        self.assistant.kill()
