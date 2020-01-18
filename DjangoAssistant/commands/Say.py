from DjangoAssistant.commands.Command import Command


class Say(Command):
    """
    Make assistant repeat the user input
    """
    recognized_commands = ['say']
    help_description = 'Have the assistant repeat what you type.'

    def respond(self):
        """
        Repeat whatever was typed after 'say'
        :return : String response based on user input
        """
        to_say = self.user_input.split(self.recognized_commands[0])[-1].strip()
        self.assistant.say(to_say)
