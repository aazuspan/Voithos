import sys
from DjangoAssistant.commands.Command import Command
from DjangoAssistant.Assistant import Assistant


class Say(Command):
    """
    Close the assistant
    """
    recognized_commands = ['bye', 'goodbye', 'close', 'exit']

    def respond(self):
        """
        Say goodbye
        """
        Assistant.say('Goodbye')
        sys.exit()
