import pytest
from enrollments.event import Event
from enrollments.member_service import MemberService


@pytest.fixture
def member_service():
    """
    Creates a MembersService object for testing.
    """
    return MemberService()

@pytest.fixture
def sample_event(member_service):
    """
    Creates an Event object for testing.
    """
    return Event("Bergsklättring", member_service)





