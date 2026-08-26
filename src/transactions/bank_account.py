
class BankAccount:
    """
    Class represents a Bank Account.
    """
    def __init__(self, logger, balance = 0):
        """
        Constructor.
        :param logger: a logger object.
        :param balance: account start balance
        """
        self.balance = balance
        self.logger = logger


    def deposit(self, amount):
        """
        Deposits the amount into the account.
        :param amount:
        """
        self.balance += amount
        self.logger.log(f"Deposit: {amount} kr, saldo {self.balance} kr")


    def withdraw(self, amount):
        """
        Withdraws the amount from the account.
        :param amount:
        :return: True/ False if successful
        """
        if self.balance >= amount:
            self.balance -= amount
            self.logger.log(f"Withdraw: {amount} kr, saldo {self.balance} kr")
            return True
        else:
            self.logger.log(f"Withdraw: kunde inte ta ut {amount} kr från kontot")
            return False