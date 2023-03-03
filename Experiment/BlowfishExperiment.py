from Crypto import Cipher
from Crypto.Cipher import Blowfish

from Experiment.Experiment import Experiment


class BlowfishExperiment(Experiment):
    def __init__(self, key: bytes, message: bytes, duration_multiplier: int = 1):
        super().__init__(message, duration_multiplier)

        self.__key = key

    def get_cipher(self) -> Cipher:
        return Blowfish.new(self.__key, Blowfish.MODE_CBC)

    def get_fields_names(self) -> tuple:
        return 'BlowFish, Crypt', 'BlowFish, Decrypt'
