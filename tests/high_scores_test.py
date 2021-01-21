import unittest

from src.high_scores import *

#Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests
    def setUp(self):
        self.scores = [1000, 3000, 2000, 3000, 400, 500, 2]

    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        expected = 2
        self.assertEqual(expected, latest(self.scores))

    # Test personal best (the highest score in the list)
    def test_highest_score(self):
        self.assertEqual(3000, personal_best(self.scores))

    # Test top three from list of scores
    def test_top_three_scores(self):
        expected = [3000, 2000, 3000]
        self.assertEqual(expected, personal_top_three(self.scores))

    # Test ordered from highest tp lowest
    def test_highest_to_lowest(self):
        expected = [3000, 2000, 3000, 1000, 500, 400, 2]
        self.assertEqual(expected, highest_to_lowest(self.scores))


    # Test top three when there is a tie
    def test_tie_top_three(self):
        expected = "There is a tie!"
        self.assertEqual(expected, tie_top_three(self.scores))

    # Test top three when there are less than three

    # Test top three when there is only one
    
