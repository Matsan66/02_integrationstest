
class MemberService:
    """
    Class representing a club members service
    """
    def __init__(self):
        """
        Constructor
        """
        self.members_list = []

    def add_member(self, member_name):
        """
        Adds a member to the club
        :param member_name: The new members name
        """
        self.members_list.append(member_name)
