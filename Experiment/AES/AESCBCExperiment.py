from Crypto import Cipher
from Crypto.Cipher import AES

from Experiment.Experiment import Experiment


class AESCBCExperiment(Experiment):
    def __init__(self, key: bytes, message: bytes, duration_multiplier: int = 1):
        super().__init__(message, duration_multiplier)

        self.__key = key

    def get_cipher(self) -> Cipher:
        return AES.new(self.__key, AES.MODE_CBC)

    def get_fields_names(self) -> tuple:
        return 'AES MODE_CBC, crypt time (ms)', 'AES MODE_CBC, decrypt time (ms)'