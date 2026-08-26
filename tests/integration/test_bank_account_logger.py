import pytest
from transactions.bank_account import BankAccount
from transactions.logger import Logger

@pytest.mark.integration
@pytest.mark.task4
def test_bank_account_logger_deposit(mocker):
    """
    Tests that the BankAccount deposit() and logger is working as intended.
    :param mocker: A mocker spy
    """
    logger = Logger()
    account = BankAccount(logger)

    spy = mocker.spy(logger, "log")

    account.deposit(100)

    spy.assert_called_once_with("Deposit: 100 kr, saldo 100 kr")
    assert "Deposit: 100 kr, saldo 100 kr" in logger.logs

    assert account.balance == 100


@pytest.mark.integration
@pytest.mark.task4
def test_bank_account_logger_withdraw(mocker, sample_logger):
    """
    Tests that the BankAccount withdraw() and logger is working as intended.
    :param mocker: A mocker spy
    """
    account = BankAccount(sample_logger, 100)

    assert account.balance == 100

    spy = mocker.spy(sample_logger, "log")

    account.withdraw(100)

    spy.assert_called_once_with("Withdraw: 100 kr, saldo 0 kr")
    assert "Withdraw: 100 kr, saldo 0 kr" in sample_logger.logs

    assert account.balance == 0


@pytest.mark.integration
@pytest.mark.task4
def test_bank_account_logger_withdraw_balance_zero(mocker, sample_logger):
    """
    Tests that the BankAccount withdraw() and logger is working as intended when balance is 0.
    :param mocker: A mocker spy
    """
    account = BankAccount(sample_logger)

    spy = mocker.spy(sample_logger, "log")

    account.withdraw(100)

    spy.assert_called_once_with("Withdraw: kunde inte ta ut 100 kr från kontot")
    assert "Withdraw: kunde inte ta ut 100 kr från kontot" in sample_logger.logs

    assert account.balance == 0


@pytest.mark.integration
@pytest.mark.task4
def test_bank_account_logger_withdraw_insufficient_balance(mocker, sample_logger):
    """
    Tests that the BankAccount withdraw() and logger is working as intended when balance is insufficient.
    :param mocker: A mocker spy
    """
    account = BankAccount(sample_logger, 200)

    spy = mocker.spy(sample_logger, "log")

    account.withdraw(300)

    spy.assert_called_once_with("Withdraw: kunde inte ta ut 300 kr från kontot")
    assert "Withdraw: kunde inte ta ut 300 kr från kontot" in sample_logger.logs

    assert account.balance ==200