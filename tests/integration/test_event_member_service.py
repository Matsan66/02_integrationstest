import pytest

@pytest.mark.integration
@pytest.mark.task2
def test_register_new_member(member_service, sample_event):
    """
    Tests that new club memeber is registered and added to the events enrolled_members list
    :param member_service: A MemberService instance
    :param sample_event:    An Event instance
    :return:
    """

    sample_event.register_new_member("Johan Larsson")
    assert "Johan Larsson" in member_service.members_list
    assert "Johan Larsson" in sample_event.enrolled_members




