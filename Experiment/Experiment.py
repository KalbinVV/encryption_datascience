import time

from Crypto import Cipher


class Experiment:
    def __init__(self, message: bytes, duration_multiplier: int):
        self.__ciphertext = None
        self.__amount_of_encrypted = None
        self.__message = message

        self.__duration_multiplier = duration_multiplier

    def get_cipher(self) -> Cipher:
        pass

    def get_fields_names(self) -> tuple:
        pass

    def test_encrypt_time(self) -> float:
        start_time = time.time()
        self.__ciphertext = self.get_cipher().encrypt(self.__message)
        duration = time.time() - start_time

        self.__amount_of_encrypted = len(self.__ciphertext)

        return duration * self.__duration_multiplier

    def test_decrypt_time(self) -> float:
        start_time = time.time()
        self.get_cipher().decrypt(self.__ciphertext)
        duration = time.time() - start_time

        return duration * self.__duration_multiplier

    def test(self) -> tuple:
        return self.test_encrypt_time(), self.test_decrypt_time()

    def process(self) -> dict:
        encrypt_time, decrypt_time = self.test()

        encrypt_field, decrypt_field = self.get_fields_names()

        return {encrypt_field: encrypt_time, decrypt_field: decrypt_time}
