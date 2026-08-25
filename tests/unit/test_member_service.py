import pytest

@pytest.mark.unit
@pytest.mark.task2
def test_add_member(member_service, mocker):
    """
    TTests that add_member() registers a new member.
    :param member_service: A MembersService instance
    :param mocker: pytest-mock fixture used to spy on add_member().
    """

    spy = mocker.spy(member_service, "add_member")

    member_service.add_member("Johan Larsson")

    spy.assert_called_once_with("Johan Larsson")
    assert "Johan Larsson" in  member_service.members_list