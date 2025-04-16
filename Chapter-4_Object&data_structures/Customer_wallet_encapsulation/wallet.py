class Wallet:
    def __init__(self, initial_value: float = 0.0):
        self._value = initial_value

    def get_total_money(self) -> float:
        return self._value

    def set_total_money(self, new_value: float):
        self._value = new_value

    def add_money(self, deposit: float):
        self._value += deposit

    def subtract_money(self, debit: float):
        self._value -= debit
