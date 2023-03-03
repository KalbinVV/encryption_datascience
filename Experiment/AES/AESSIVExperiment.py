from Crypto import Cipher
from Crypto.Cipher import AES

from Experiment.Experiment import Experiment


class AESSIVExperiment(Experiment):
    def __init__(self, key: bytes, message: bytes, duration_multiplier: int = 1):
        super().__init__(message, duration_multiplier)

        self.__key = key

    def get_cipher(self) -> Cipher:
        return AES.new(self.__key, AES.MODE_SIV)

    def get_fields_names(self) -> tuple:
        return 'AES MODE_SIV, crypt time (ms)', 'AES MODE_SIV, decrypt time (ms)'