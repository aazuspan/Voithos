import unittest
from Voithos.Voithos import Voithos
from Voithos.commands.RollDice import RollDice


class RollDiceTest(unittest.TestCase):
    voithos = Voithos()
    test_cmd = RollDice(request_dict=None, voithos=voithos)

    def test_single_die_parsing(self):
        """
        Test that a single die is correctly parsed
        """
        self.assertTrue(self.test_cmd.parse_die('roll d20'), [(1, 20)])

    def test_multiple_same_dice_parsing(self):
        """
        Test that multiple die of the same value are correctly parsed
        """
        self.assertTrue(self.test_cmd.parse_die('roll 4d20 and 2d6'), [(4, 20), (2, 6)])

    def test_multiple_different_dice_parsing(self):
        """
        Test that multiple die of different values are correctly parsed
        """
        self.assertTrue(self.test_cmd.parse_die('roll 4d20'), [(4, 20)])

    def test_no_dice_parsing(self):
        """
        Test that parsing a request with no valid die returns nothing
        """
        self.assertFalse(self.test_cmd.parse_die('roll 234 fdl 23trls a3d'))

    def test_rolling_dice(self):
        """
        Test that various random dice rolls always fall within valid range over many rolls
        """
        dice = [(1, 20), (2, 6), (10, 10), (4, 3), (5, 8), (1, 90)]

        for die in dice:
            num = die[0]
            val = die[1]
            min = num
            max = num * val

            for i in range(1000):
                roll = self.test_cmd.roll_dice(num, val)
                try:
                    self.assertTrue(min <= roll <= max)
                except AssertionError:
                    raise AssertionError(f'Dice roll out of range! {num}d{val} rolled {roll}.')


if __name__ == '__main__':
    unittest.main()
