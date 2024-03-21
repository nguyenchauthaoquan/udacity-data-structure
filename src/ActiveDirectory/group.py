class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        if group is not None:
            self.groups.append(group)

    def add_user(self, user):
        if user is not None and len(user.strip()) > 0:
            self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    users = group.get_users()

    if user in users:
        return True
    else:
        groups = group.get_groups()
        for group_item in groups:
            if is_user_in_group(user, group_item):
                return True
        return False


empty_group = Group("empty group")
user = "user"

print(empty_group.get_name(), "group has user?", is_user_in_group(user, empty_group))

group_1 = Group("group 1")
group_1.add_user("user1")
group_1.add_user("user2")
group_1.add_user("user3")
group_1.add_user("user4")

print(group_1.get_name(), "group has user?", is_user_in_group("user1", group_1))
print(group_1.get_name(), "group has user?", is_user_in_group("user2", group_1))
print(group_1.get_name(), "group has user?", is_user_in_group("user3", group_1))
print(group_1.get_name(), "group has user?", is_user_in_group("user4", group_1))
print(group_1.get_name(), "group has user?", is_user_in_group("user1", group_1))

group_2 = Group("group 2")

group_2.add_user("user5")
group_2.add_user("user6")
group_2.add_user("user7")
group_2.add_user("user8")
group_2.add_group(group_1)

print(group_1.get_name(), "group has user?", is_user_in_group("user1", group_2))
print(group_1.get_name(), "group has user?", is_user_in_group("user2", group_2))
print(group_1.get_name(), "group has user?", is_user_in_group("user3", group_2))
print(group_1.get_name(), "group has user?", is_user_in_group("user4", group_2))

print(group_1.get_name(), "group has user?", is_user_in_group("user5", group_2))
print(group_1.get_name(), "group has user?", is_user_in_group("user6", group_2))
print(group_1.get_name(), "group has user?", is_user_in_group("user7", group_2))
print(group_1.get_name(), "group has user?", is_user_in_group("user8", group_2))
print(group_1.get_name(), "group has user?", is_user_in_group("user9", group_2))
