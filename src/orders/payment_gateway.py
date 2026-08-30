class PaymentGateway:
    """
    Represents a payment gateway
    """

    def execute_payment(self, amount):
        """
        Executes the payment.
        :param amount: The amount to be paid.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            return False

        return True