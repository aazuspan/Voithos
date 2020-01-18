from DjangoAssistant.commands.Command import Command
from DjangoAssistant.Assistant import Assistant


class Say(Command):
    """
    Make assistant repeat the user input
    """
    recognized_commands = ['say']

    def respond(self):
        """
        Repeat whatever was typed after 'say'
        :return : String response based on user input
        """
        to_say = self.user_input.split(self.recognized_commands[0])[-1].strip()
        Assistant.say(to_say)
