from Voithos.commands.Command import Command


class Say(Command):
    """
    Make Voithos repeat the user input
    """
    name = 'say'
    utterances = [
        'say this',
        'please say this',
        'can you say a sentence?',
        'hey Voithos, say "Im a little fat girl"'
    ]
    help_description = 'Have Voithos repeat what you type.'

    def respond(self):
        """
        Repeat whatever was typed after 'say'
        """
        response = self.user_input.split('say')[-1].strip()
        if not response:
            response = "Say what?"

        return response
