from Crypto import Cipher
from Crypto.Cipher import AES

from Experiment.Experiment import Experiment


class AESGCMExperiment(Experiment):
    def __init__(self, key: bytes, message: bytes, duration_multiplier: int = 1, amount_of_cycles: int = 1):
        super().__init__(message, duration_multiplier, amount_of_cycles)

        self.__key = key

    def get_cipher(self) -> Cipher:
        return AES.new(self.__key, AES.MODE_GCM)

    def get_fields_names(self) -> tuple:
        return 'AES MODE_GCM, Время шифрования (с)', 'AES MODE_GCM, Время расшифрования (с)'
