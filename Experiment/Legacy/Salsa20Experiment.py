from Crypto import Cipher
from Crypto.Cipher import Salsa20

from Experiment.Experiment import Experiment


class Salsa20Experiment(Experiment):
    def __init__(self, key: bytes, message: bytes, duration_multiplier: int = 1, amount_of_cycles: int = 1):
        super().__init__(message, duration_multiplier, amount_of_cycles)

        self.__key = key

    def get_cipher(self) -> Cipher:
        return Salsa20.new(self.__key)

    def get_fields_names(self) -> tuple:
        return 'Salsa20, Время шифрования (с)', 'Salsa20, Время расшифрвания (с)'
