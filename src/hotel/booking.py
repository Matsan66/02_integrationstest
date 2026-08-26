class Booking:
    """
    Class representing a room booking.
    """
    def __init__(self, guest, room, payment):
        """
        Constructor.
        :param guest:
        :param room:
        :param payment:
        """
        self.guest = guest
        self.room = room
        self.payment = payment

    def confirm_booking(self):
        """
        Method that confirms the booking.
        :return: True or False depending on if the booking and payment were successful.
        """
        if not self.room.is_available:
            return False

        if not self.payment.pay(self.room.price):
            return False

        return self.room.book()
