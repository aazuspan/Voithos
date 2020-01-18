from commands.Command import Command


class Repeat(Command):
    """
    Make Voithos repeat what was last said by the Voithos
    """
    recognized_commands = ['repeat']
    help_description = 'Repeat the last thing Voithos said.'

    def respond(self):
        """
        Repeat whatever was last said
        """
        self.voithos.say(self.voithos.last_said)
