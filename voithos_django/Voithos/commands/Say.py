from Voithos.commands.Command import Command


class Say(Command):
    """
    Make Voithos repeat the user input
    """
    recognized_keywords = ['say']
    help_description = 'Have Voithos repeat what you type.'
    utterances = [
        'say this',
        'please say this',
        'can you say a sentence?',
        'hey Voithos, say "Im a little fat girl"'
    ]
    name = 'say'

    def respond(self):
        """
        Repeat whatever was typed after 'say'
        """
        response = self.user_input.split(self.recognized_keywords[0])[-1].strip()
        if not response:
            response = "Say what?"

        return response
