import pytest
from hotel.guest import Guest
from hotel.payment import Payment
from hotel.booking import Booking


@pytest.mark.integration
@pytest.mark.task1
def test_booking_payment_successful(sample_room, mocker):
    """
    Tests that the booking payment is successful
    :param mocker:
    """
    guest = Guest(
        "John Petterson",
        "072-1234567",
        "john.petterson@provider.se"
    )
    payment = Payment()
    booking = Booking(guest, sample_room, payment)

    spy = mocker.spy(payment, "pay")

    assert booking.confirm_booking() is True
    spy.assert_called_once_with(1500)
    assert sample_room.is_available is False


@pytest.mark.integration
@pytest.mark.task1
def test_booking_payment_failed(sample_room, mocker):
    """
    Tests that a room is not booked if payment fails
    :param mocker:
    :return:
    """
    guest = Guest(
        "John Petterson",
        "072-1234567",
        "john.petterson@provider.se"
    )
    payment = Payment(False)
    booking = Booking(guest, sample_room, payment)

    spy = mocker.spy(payment, "pay")

    assert booking.confirm_booking() is False
    spy.assert_called_once_with(1500)
    assert sample_room.is_available is True

@pytest.mark.integration
@pytest.mark.task1
def test_booking_room_occupied_payment_not_made(sample_room, mocker):
    """
    Tests that no payment is done if a room is occupied
    :param mocker:
    :return:
    """
    guest = Guest(
        "John Petterson",
        "072-1234567",
        "john.petterson@provider.se"
    )
    sample_room.book()
    payment = Payment()
    booking = Booking(guest, sample_room, payment)

    spy = mocker.spy(payment, "pay")

    assert booking.confirm_booking() is False
    spy.assert_not_called()
    assert sample_room.is_available is False