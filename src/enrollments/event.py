
class Event:
    """
    Event class represents a single event
    """
    def __init__(self, event_name, member_service):
        """
        Event constructor
        :param event_name: The name of the event
        :param member_service: A MemberService instance
        """
        self.event_name = event_name
        self.member_service = member_service
        self.enrolled_members = []


    def register_new_member(self, member_name):
        """
        Register a new club member and adds it to the enrolled_members list
        :param member_name: The new member name
        """
        self.member_service.add_member(member_name)
        self.enrolled_members.append(member_name)


    def sign_up(self, member_name):
        """
        Signs up member to the event by adding it to the enrolled_members list
        :param member_name: The member to enroll
        """
        self.enrolled_members.append(member_name)

