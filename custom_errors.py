class account_not_found(Exception):
    def __init__(self):
        super().__init__("No matching account found.")

    def __str__(self):
        return f"{self.message}"

class not_enough_funds(Exception):
    def __init__(self):
        super().__init__("Sender doesn't have enough funds.")

    def __str__(self):
        return f"{self.message}"