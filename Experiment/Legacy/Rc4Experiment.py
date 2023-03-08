from Crypto import Cipher
from Crypto.Cipher import ARC2

from Experiment.Experiment import Experiment


class Rc4Experiment(Experiment):
    def __init__(self, key: bytes, message: bytes, duration_multiplier: int = 1, amount_of_cycles: int = 1):
        super().__init__(message, duration_multiplier, amount_of_cycles)

        self.__key = key

    def get_cipher(self) -> Cipher:
        return ARC2.new(self.__key, ARC2.MODE_CFB)

    def get_fields_names(self) -> tuple:
        return 'RC4, Время шифрования (с)', 'RC4, Время расшифрования (с)'
