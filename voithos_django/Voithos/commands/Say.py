from Voithos.commands.Command import Command


class Say(Command):
    """
    Make Voithos repeat the user input
    """
    recognized_keywords = ['say']
    help_description = 'Have Voithos repeat what you type.'

    def respond(self):
        """
        Repeat whatever was typed after 'say'
        """
        to_say = self.user_input.split(self.recognized_keywords[0])[-1].strip()
        return to_say
