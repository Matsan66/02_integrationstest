class Logger:
    """
    Class representing a transaction log
    """
    def __init__(self):
        self.logs = []

    def log(self, transaction_log):
        """
        Logs a transaction in the logs list
        :param transaction_log:
        """
        self.logs.append(transaction_log)