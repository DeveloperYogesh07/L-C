from wallet import Wallet

class Customer:
    def __init__(self, first_name: str, last_name: str, initial_balance: float):
        self.first_name = first_name
        self.last_name = last_name
        self._wallet = Wallet(initial_balance)

    def get_first_name(self) -> str:
        return self.first_name

    def get_last_name(self) -> str:
        return self.last_name

    def make_payment(self, amount: float) -> bool:
        if self._wallet.get_total_money() >= amount:
            self._wallet.subtract_money(amount)
            return True
        return False

    def add_money(self, amount: float):
        self._wallet.add_money(amount)

    def get_balance(self) -> float:
        return self._wallet.get_total_money()
