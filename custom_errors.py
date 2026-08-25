"""Dit zijn error messages, speciaal voor dit programma."""
class AccountNotFound(Exception):
    """Deze error triggert wanneer een account niet gevonden wordt in een querry."""
    def __init__(self):
        super().__init__("No matching account found.")
        self.message = "No matching account found."

    def __str__(self):
        return f"{self.message}"

class NotEnoughFunds(Exception):
    """Deze error triggert wanneer een gebruiker niet genoeg geld heeft voor een transactie."""
    def __init__(self):
        super().__init__("Sender doesn't have enough funds.")
        self.message = "Sender doesn't have enough funds."

    def __str__(self):
        return f"{self.message}"