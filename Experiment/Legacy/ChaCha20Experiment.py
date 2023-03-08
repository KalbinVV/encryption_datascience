from Crypto import Cipher
from Crypto.Cipher import ChaCha20

from Experiment.Experiment import Experiment


class ChaCha20Experiment(Experiment):
    def __init__(self, key: bytes, message: bytes, duration_multiplier: int = 1, amount_of_cycles: int = 1):
        super().__init__(message, duration_multiplier, amount_of_cycles)

        self.__key = key

    def get_cipher(self) -> Cipher:
        return ChaCha20.new(key=self.__key)

    def get_fields_names(self) -> tuple:
        return 'ChaCha20, Время шифрования (с)', 'ChaCha20, Время расшифрования (с)'
