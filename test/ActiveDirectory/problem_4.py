import unittest

from parameterized import parameterized

from src.ActiveDirectory.group import Group, is_user_in_group


class MyTestCase(unittest.TestCase):
    @parameterized.expand([
        ["user1"],
        ["user2"],
        ["user3"],
    ])
    def test_edge_cases_1(self, user):
        group = Group("testing group")

        group.add_user(user)
        self.assertTrue(is_user_in_group(user, group))

    @parameterized.expand([
        ["user1", "user2"],
        ["user3", "user4"],
        ["user5", "user6"],
    ])
    def test_edge_cases_2(self, exist_user, non_exist_user):
        group = Group("testing group 2")
        group.add_user(exist_user)
        self.assertTrue(is_user_in_group(exist_user, group))
        self.assertFalse(is_user_in_group(non_exist_user, group))

    @parameterized.expand([
        ["user1", "user2"],
        ["user3", "user4"],
        ["user5", "user6"],
    ])
    def test_edge_cases_3(self, user, sub_user):
        group = Group("testing group 3")
        sub_group = Group("sub testing group 1")
        group.add_user(user)
        sub_group.add_user(sub_user)
        group.add_group(sub_group)

        self.assertTrue(is_user_in_group(user, group))
        self.assertFalse(is_user_in_group(user, sub_group))
        self.assertTrue(is_user_in_group(sub_user, group))
        self.assertTrue(is_user_in_group(sub_user, sub_group))

    @parameterized.expand([
        [""],
        [" "],
        [None]
    ])
    def test_empty_or_null_cases_1(self, user):
        group = Group("testing group 4")
        group.add_user(user)

        self.assertFalse(is_user_in_group(user, group))

    @parameterized.expand([
        ["", ""],
        [" ", " "],
        [None, None]
    ])
    def test_empty_or_null_cases_2(self, user, sub_user):
        group = Group("testing group 4")
        sub_group = Group("sub testing group 2")
        group.add_user(user)
        sub_group.add_user(sub_user)
        group.add_group(sub_group)

        self.assertFalse(is_user_in_group(user, group))
        self.assertFalse(is_user_in_group(user, sub_group))
        self.assertFalse(is_user_in_group(sub_user, group))
        self.assertFalse(is_user_in_group(sub_user, sub_group))

if __name__ == '__main__':
    unittest.main()
