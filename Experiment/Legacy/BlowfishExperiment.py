from Crypto import Cipher
from Crypto.Cipher import Blowfish

from Experiment.Experiment import Experiment


class BlowfishExperiment(Experiment):
    def __init__(self, key: bytes, message: bytes, duration_multiplier: int = 1, amount_of_cycles: int = 1):
        super().__init__(message, duration_multiplier, amount_of_cycles)

        self.__key = key

    def get_cipher(self) -> Cipher:
        return Blowfish.new(self.__key, Blowfish.MODE_EAX)

    def get_fields_names(self) -> tuple:
        return 'BlowFish, Время шифрования (с)', 'BlowFish, Время расшифрования (с)'
