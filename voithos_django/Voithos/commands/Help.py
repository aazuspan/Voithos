from Voithos.commands.Command import Command


class Help(Command):
    """
    Print a list of all possible commands
    """
    recognized_keywords = ['help']
    help_description = 'Display a list of all commands and their descriptions.'
    utterances = [
        'help',
        'what can you do?',
        'what is this?',
        'command list',
        'what commands can I do?',
        'what should I type',
        'help me',
        'please help',
        'how to use this?',
    ]
    name = 'help'

    def respond(self):
        """
        Get help information from each command and return it all
        """
        response = '<h4>COMMANDS</h4></b>'

        for cmd in self.voithos.cmd_handler.cmd_list:
            response += cmd.help() + '<br>'

        return response
