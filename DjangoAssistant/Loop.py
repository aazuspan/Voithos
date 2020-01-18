from Assistant import Assistant


class Loop:
    """
    This class controls the main program loop of user input and assistant response
    """
    def __init__(self):
        self.assistant = Assistant()
        self.run()

    def run(self):
        while True:
            user_input = input(self.assistant.prompt())
            self.assistant.respond(user_input)


if __name__ == '__main__':
    loop = Loop()
