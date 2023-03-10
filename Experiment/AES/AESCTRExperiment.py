from Crypto import Cipher
from Crypto.Cipher import AES

from Experiment.Experiment import Experiment


class AESCTRExperiment(Experiment):
    def __init__(self, key: bytes, message: bytes, duration_multiplier: int = 1, amount_of_cycles: int = 1):
        super().__init__(message, duration_multiplier, amount_of_cycles)

        self.__key = key

    def get_cipher(self) -> Cipher:
        return AES.new(self.__key, AES.MODE_CTR)

    def get_fields_names(self) -> tuple:
        return 'AES MODE_CTR, Время шифрования (с)', 'AES MODE_CTR, Время расшифрования (с)'
