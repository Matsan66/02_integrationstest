class Payment:
    """
    Class to represent a payment.
    """
    def __init__(self, successful = True):
        """
        Constructor.
        :param successful:
        """
        self.successful = successful

    def pay(self, amount):
        """
        Method to pay a hotel room.
        :param amount:
        :return: If payment is successful, return true, else return false.
        """
        return self.successful
