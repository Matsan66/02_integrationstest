import pytest
from enrollments.event import Event
from enrollments.member_service import MemberService
from shoppingcart.inventory import Inventory
from transactions.logger import Logger
from hotel.room import Room


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

@pytest.fixture
def sample_inventory():
    """
    Creates an inventory object for testing.
    """
    return Inventory()

@pytest.fixture
def sample_logger():
    """
    Creates a logger object for testing.
    """
    return Logger()

@pytest.fixture
def sample_room():
    """
    Creates a payment object for testing.
    """
    return Room(101, 1500)







