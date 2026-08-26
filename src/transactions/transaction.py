class Transaction:
    """
    Class representing a transaction.
    """

    def transfer(self, amount, from_account, to_account):
        """
        Performs a transfer between two accounts.
        :param amount: The amount to transfer.
        :param from_account: The account to transfer from.
        :param to_account: The account to transfer to.
        """
        if from_account.withdraw(amount):
            to_account.deposit(amount)




