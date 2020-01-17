from DjangoAssistant.commands.Command import Command


class Say(Command):
    """
    Make assistant repeat the user input
    """
    recognized_command = 'say'

    def respond(self):
        """
        Repeat whatever was typed after 'say'
        :return : String response based on user input
        """
        to_say = self.user_input.split(self.recognized_command)[-1]

        return to_say


