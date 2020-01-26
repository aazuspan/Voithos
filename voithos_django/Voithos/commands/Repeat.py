from Voithos.commands.Command import Command


class Repeat(Command):
    """
    Make Voithos repeat what was last said by Voithos
    """
    recognized_keywords = ['repeat']
    help_description = 'Repeat the last thing Voithos said.'
    name = 'repeat'

    def respond(self):
        """
        Repeat whatever was last said
        """
        response = self.voithos.last_said

        if not response:
            response = "I haven't said anything yet"

        return response
