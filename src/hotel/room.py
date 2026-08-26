class Room:
    """
    Class representing a room.
    """
    def __init__(self, number, price):
        """
        Constructor.
        :param number:
        :param price:
        """
        self.number = number
        self.price = price
        self.is_available = True

    def book(self):
        """
        Method to book the room.
        :return: True or False depending on whether the room is available.
        """
        if not self.is_available:
            return False

        self.is_available = False
        return True

    def release(self):
        """
        Method to release the room.
        """
        self.is_available = True