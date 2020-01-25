import random
import re
from Voithos.commands.Command import Command


class RollDice(Command):
    """
    Voithos rolls a die
    """
    recognized_keywords = ['roll']
    help_description = 'Have Voithos roll a die. Example: "roll a d20" or "roll 4d6" or "roll 4d6 and 2d12"'

    def respond(self):
        """
        Return the sum of dice rolls
        """
        dice = self.parse_die(self.user_input)
        dice_sum = 0

        if not dice:
            response = 'Sorry, that input was invalid. To roll random dice, please say something like "roll 2d20" or' \
                       '"roll a d6".'
        else:
            for die in dice:
                dice_sum += self.roll_dice(die[0], die[1])
            response = dice_sum

        return response

    @staticmethod
    def parse_die(user_input):
        """
        Parse input text to find patterns that match '2d6'
        :param user_input: A raw string submitted by the user
        :return: List of tuples of ints. First int is number of die. Second int is value of die. Multiple die can be
        parsed and returned (eg. "2d6 and 4d10" returns [(2, 6), (4, 10)]). If number of dice is not entered, 1 will be
        assumed (eg. d6 = [(1, 6)]).
        """
        die_pattern = re.compile(r'''(\d*)d(\d+)''')
        dice = re.findall(die_pattern, user_input)
        parsed_dice = []

        # Dice nums and vals will be strings and need to be converted to ints
        for die in dice:
            try:
                if die[0]:
                    num = int(die[0])
                else:
                    num = 1
                val = int(die[1])

                parsed_dice.append((num, val))
            except TypeError:
                pass

        return parsed_dice

    @staticmethod
    def roll_dice(num, val):
        """
        Roll a number of dice of a given value
        :param num: Number of dice
        :param val: Value of dice
        :return: Sum of dice rolls
        """
        dice_sum = 0

        for die in range(num):
            dice_sum += random.randint(1, val)

        return dice_sum
