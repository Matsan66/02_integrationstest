import pytest
from hotel.booking import Booking
from hotel.guest import Guest
from hotel.payment import Payment

@pytest.mark.integration
@pytest.mark.task1
def test_booking_room_available(sample_room):
    """
    Tests that it's possible to book an available room.
    """
    guest = Guest(
        "John petterson",
        "072-1234567",
        "john.petterson@provider.se"
    )
    payment = Payment()
    booking = Booking(guest, sample_room, payment)

    result = booking.confirm_booking()

    assert result is True
    assert sample_room.is_available is False


@pytest.mark.integration
@pytest.mark.task1
def test_booking_room_not_available(sample_room):
    """
    Tests that it's not possible to book an occupied room.
    """
    guest = Guest(
        "John petterson",
        "072-1234567",
        "john.petterson@provider.se"
    )

    first_booking = Booking(guest, sample_room, payment = Payment())
    assert first_booking.confirm_booking() is True

    second_booking = Booking(guest, sample_room, payment = Payment())
    assert second_booking.confirm_booking() is False

    assert sample_room.is_available is False