from Voithos import Voithos


class Loop:
    """
    This class controls the main program loop of user input and Voithos response
    """
    def __init__(self):
        self.voithos = Voithos()
        self.run()

    def run(self):
        while True:
            user_input = input(self.voithos.prompt())
            self.voithos.respond(user_input)


if __name__ == '__main__':
    loop = Loop()
