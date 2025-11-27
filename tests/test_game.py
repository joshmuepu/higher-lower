import unittest
from game_data import data
import main


class TestGame(unittest.TestCase):
    def test_validate_data_ok(self):
        main.validate_data()  # should not raise

    def test_get_random_account_distinct(self):
        a = main.get_random_account()
        b = main.get_random_account(exclude=a)
        self.assertNotEqual(a, b)

    def test_compare_followers_correct_a(self):
        acc_a = {'name': 'A', 'follower_count': 10, 'description': '', 'country': ''}
        acc_b = {'name': 'B', 'follower_count': 5, 'description': '', 'country': ''}
        is_correct, auto, picked_a, tie = main.compare_followers(acc_a, acc_b, 'a')
        self.assertTrue(is_correct)
        self.assertTrue(picked_a)
        self.assertFalse(tie)
        self.assertFalse(auto)

    def test_compare_followers_correct_b(self):
        acc_a = {'name': 'A', 'follower_count': 3, 'description': '', 'country': ''}
        acc_b = {'name': 'B', 'follower_count': 7, 'description': '', 'country': ''}
        is_correct, auto, picked_a, tie = main.compare_followers(acc_a, acc_b, 'b')
        self.assertTrue(is_correct)
        self.assertFalse(picked_a)
        self.assertFalse(tie)
        self.assertFalse(auto)

    def test_compare_followers_tie(self):
        acc_a = {'name': 'A', 'follower_count': 5, 'description': '', 'country': ''}
        acc_b = {'name': 'B', 'follower_count': 5, 'description': '', 'country': ''}
        is_correct, auto, picked_a, tie = main.compare_followers(acc_a, acc_b, 'a')
        self.assertTrue(is_correct)
        self.assertTrue(tie)
        self.assertTrue(auto)
        is_correct2, auto2, picked_a2, tie2 = main.compare_followers(acc_a, acc_b, 'b')
        self.assertTrue(is_correct2)
        self.assertTrue(tie2)
        self.assertTrue(auto2)

    def test_data_structure_keys(self):
        required = {"name", "follower_count", "description", "country"}
        for entry in data:
            self.assertTrue(required.issubset(entry.keys()))


if __name__ == '__main__':
    unittest.main()

