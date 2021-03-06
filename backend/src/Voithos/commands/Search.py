import re
from Voithos.commands.Command import Command


class Search(Command):
    """
    Return link to google search
    """
    name = 'search'
    utterances = [
        'Search for Indiana Jones movies',
        'search how long chickens live?',
        'please search for Rolling Stones Satisfaction',
        'find how many quarts in a cup',
        'find how to train goldfish',
        'please find goldfish recipe',
        'look up local news',
        'look up where is the closest resteraunt',
        'please look up how to spell resteraunt'
    ]
    help_description = 'Have Voithos perform a google search.'

    def respond(self):
        """
        Perform a google search and return a url link for the results
        """
        # TODO: Split the user input to only search words that come after the command
        search_terms = self.user_input
        cleaned_search_terms = self.urlify(search_terms)
        search_url = self.build_search_url(cleaned_search_terms)
        search_link = self.build_link(search_url)

        return search_link

    def urlify(self, input_string):
        """
        Reformat a string to be URL friendly
        :param input_string: A user-submitted string
        :return : The input string with all special characters removed and whitespace replaced with +
        """
        # Remove everything that isn't alphanumeric or whitespace
        s = re.sub(r"[^\w\s]", '', input_string)

        # Replace all whitespace
        s = re.sub(r"\s+", '+', input_string)

        return s

    @staticmethod
    def build_search_url(search_terms):
        """
        Build a URL to automate a Google search
        :param search_terms: A cleaned input string
        :return: A URL for a Google search of the search terms
        """
        return f'https://google.com/search?q={search_terms}'

    @staticmethod
    def build_link(search_url):
        """
        Make a url into a markup link tag
        :param search_url: A URL string
        :return: A URL string inside an HTML 'a' tag
        """
        return f'<a href="{search_url}">{search_url}</a>'
