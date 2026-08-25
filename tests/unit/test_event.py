import pytest

@pytest.mark.unit
@pytest.mark.task2
def test_sign_up(sample_event):
    """
    Tests that sign_up() method correctly adds a member to an events enrolled_members list
    :param sample_event: An Event instance
    """

    sample_event.sign_up("Johan Larsson")

    assert "Johan Larsson" in sample_event.enrolled_members



