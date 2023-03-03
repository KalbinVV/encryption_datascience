import random

import Crypto.Random.random

from Experiment.ExperimentEnum import ExperimentEnum
from Utils.Utils import Utils


class ExperimentsPolygon:
    def __init__(self, experiments_enums: list, amount_of_experiments: int,
                 keys_length_array: list, max_length_of_message: int, duration_multiplier: int = 1):
        self.__experiments_enums = experiments_enums
        self.__amount_of_experiments = amount_of_experiments
        self.__max_length_of_message = max_length_of_message
        self.__duration_multiplier = duration_multiplier
        self.__keys_length_array = keys_length_array

    def process(self):
        size_of_key_field = 'Size of key'
        size_of_message_field = 'Size of message'

        result_dictionary = {
            size_of_key_field: [],
            size_of_message_field: []
        }

        for _ in range(self.__amount_of_experiments):
            message_length = random.randint(1, self.__max_length_of_message + 1)
            message = Crypto.Random.get_random_bytes(message_length)

            key_length = self.__keys_length_array[0]
            key = Crypto.Random.get_random_bytes(key_length)

            result_dictionary[size_of_message_field].append(len(message))
            result_dictionary[size_of_key_field].append(len(key))

            for experiment_enum in self.__experiments_enums:
                experiment_class = ExperimentEnum.from_enum(experiment_enum)
                experiment = experiment_class(key, message, duration_multiplier=self.__duration_multiplier)

                experiment_result = experiment.process()

                result_dictionary = Utils.union_dicts(result_dictionary, experiment_result)

        return result_dictionary
