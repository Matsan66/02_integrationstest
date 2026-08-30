class Order:
    """
    represents an order
    """
    orders = []

    def __init__(self, product, price):
        """
        Initializes the order
        :param product: The product ordered
        :param price: The price of the order
        """
        self.product = product
        self.price = price
        self.status = "unpaid"

        Order.orders.append({
            "product": self.product,
            "price": self.price
        })


    def make_payment(self, payment_gateway_mock):

        """
        Makes a payment for the order
        :param payment_gateway_mock: Payment gateway used to process payment
        """
        if payment_gateway_mock.execute_payment(self.price):
            self.status = "paid"
        else:
            self.status = "error"




