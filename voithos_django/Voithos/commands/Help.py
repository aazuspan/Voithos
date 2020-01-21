from Voithos.commands.Command import Command


class Help(Command):
    """
    Print a list of all possible commands
    """
    recognized_keywords = ['help', '?']
    help_description = 'Display a list of all commands and their descriptions.'

    def respond(self):
        """
        Get help information from each command and return it all
        """
        response = '___COMMANDS___'

        for cmd in self.voithos.cmd_handler.cmds:
            response += cmd.help()

        return response
