import pytest
from orders.order import Order
from orders.payment_gateway import PaymentGateway

@pytest.fixture
def payment_gateway_mock(mocker):
    return mocker.Mock(spec = PaymentGateway)


@pytest.mark.integration
@pytest.mark.task5
def test_order_payment_gateway_valid_amount(mocker, payment_gateway_mock):
    """
    Tests that the order status is set to "paid" when the payment succeeds.
    :param mocker: pytest mocker fixture.
    :param payment_gateway_mock: Mocked payment gateway.
    """
    payment_gateway_mock.execute_payment.return_value = True
    spy = mocker.spy(payment_gateway_mock, "execute_payment")

    order = Order("Bromsskiva", 850)
    order.make_payment(payment_gateway_mock)

    spy.assert_called_once_with(850)
    assert order.status == "paid"


@pytest.mark.integration
@pytest.mark.task5
def test_order_payment_gateway_failure(mocker, payment_gateway_mock):
    """
    Tests that the order status is set to "error" when the payment fails.
    :param mocker: pytest mocker fixture.
    :param payment_gateway_mock: Mocked payment gateway.
    """

    payment_gateway_mock.execute_payment.return_value = False
    spy = mocker.spy(payment_gateway_mock, "execute_payment")

    order = Order("Bromsskiva", 850)
    order.make_payment(payment_gateway_mock)

    spy.assert_called_once_with(850)
    assert order.status == "error"