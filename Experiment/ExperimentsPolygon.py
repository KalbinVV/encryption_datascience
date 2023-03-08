import random

import Crypto.Random.random

from Experiment.ExperimentEnum import ExperimentEnum
from Utils.Utils import Utils


class ExperimentsPolygon:
    def __init__(self, experiments_enums: list, amount_of_experiments: int,
                 keys_length_array: list, max_length_of_message: int, duration_multiplier: int = 1,
                 max_amount_of_cycles: int = 1):
        self.__experiments_enums = experiments_enums
        self.__amount_of_experiments = amount_of_experiments
        self.__max_length_of_message = max_length_of_message
        self.__duration_multiplier = duration_multiplier
        self.__keys_length_array = keys_length_array
        self.__max_amount_of_cycles = max_amount_of_cycles

    def process(self):
        size_of_key_field = 'Размер ключа (биты)'
        size_of_message_field = 'Размер сообщения (биты)'
        amount_of_cycles_field = 'Количество циклов'
        amount_of_zero_bits_in_key_field = 'Количество нулевых битов в записи ключа'
        amount_of_unit_bits_in_key_field = 'Количество отличных от нуля битов в записи ключа'
        amount_of_zero_bits_in_message_field = 'Количество нулевых битов в записи сообщения'
        amount_of_unit_bits_in_message_field = 'Количество отличных от нуля битов в записи сообщения'

        result_dictionary = {
            size_of_key_field: [],
            size_of_message_field: [],
            amount_of_cycles_field: [],
            amount_of_zero_bits_in_key_field: [],
            amount_of_unit_bits_in_key_field: [],
            amount_of_zero_bits_in_message_field: [],
            amount_of_unit_bits_in_message_field: []
        }

        for _ in range(self.__amount_of_experiments):
            message_length = random.randint(1, self.__max_length_of_message + 1)
            message = Crypto.Random.get_random_bytes(message_length)

            key_length = self.__keys_length_array[random.randint(0, len(self.__keys_length_array) - 1)]
            key = Crypto.Random.get_random_bytes(key_length)

            result_dictionary[size_of_message_field].append(len(message))
            result_dictionary[size_of_key_field].append(len(key))

            amount_of_zero_bits_in_key = key.count(0)
            amount_of_zero_bits_in_message = message.count(0)

            result_dictionary[amount_of_zero_bits_in_key_field].append(amount_of_zero_bits_in_key)
            result_dictionary[amount_of_unit_bits_in_key_field].append(len(key) - amount_of_zero_bits_in_key)

            result_dictionary[amount_of_zero_bits_in_message_field].append(amount_of_zero_bits_in_message)
            result_dictionary[amount_of_unit_bits_in_message_field].append(len(message) - amount_of_zero_bits_in_message)

            amount_of_cycles = random.randint(1, self.__max_amount_of_cycles + 1)

            result_dictionary[amount_of_cycles_field].append(amount_of_cycles)

            for experiment_enum in self.__experiments_enums:
                experiment_class = ExperimentEnum.from_enum(experiment_enum)
                experiment = experiment_class(key, message, duration_multiplier=self.__duration_multiplier,
                                              amount_of_cycles=amount_of_cycles)

                experiment_result = experiment.process()

                result_dictionary = Utils.union_dicts(result_dictionary, experiment_result)

        return result_dictionary
