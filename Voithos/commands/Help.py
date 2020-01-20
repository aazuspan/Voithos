from commands.Command import Command


class Help(Command):
    """
    Print a list of all possible commands
    """
    recognized_commands = ['help', '?']
    help_description = 'Display a list of all commands and their descriptions.'

    def respond(self):
        """
        Have each command display it's help information
        """
        self.voithos.say('___COMMANDS___')

        for cmd in self.voithos.cmd_handler.cmds:
            cmd.help()