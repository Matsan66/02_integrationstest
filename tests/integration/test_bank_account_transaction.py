import pytest
from transactions.bank_account import BankAccount
from transactions.transaction import Transaction

@pytest.mark.integration
@pytest.mark.task4
def test_bank_account_transaction_successful(sample_logger):
    """
    Tests that a transfer of money between two accounts is successful.
    :param sample_logger:
    """
    transaction = Transaction()

    to_account = BankAccount(sample_logger)
    from_account = BankAccount(sample_logger, 500)

    transaction.transfer(200, from_account, to_account)

    assert from_account.balance == 300
    assert to_account.balance == 200


@pytest.mark.integration
@pytest.mark.task4
def test_bank_account_transaction_insufficient_balance(sample_logger):
    """
    Tests that a transfer between two accounts is not performed if insufficient funds on from_account
    :param sample_logger:
    """
    transaction = Transaction()

    to_account = BankAccount(sample_logger, 200)
    from_account = BankAccount(sample_logger, 100)

    transaction.transfer(200, from_account, to_account)

    assert from_account.balance == 100
    assert to_account.balance == 200
