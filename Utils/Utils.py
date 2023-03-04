import copy

import numpy as np
import pandas as pd

class Utils:
    @staticmethod
    def union_dicts(first_dict: dict, second_dict: dict):
        if len(first_dict) == 0:
            return second_dict
        elif len(second_dict) == 0:
            return first_dict

        joint_dictionary = first_dict | second_dict

        for key in joint_dictionary.keys():
            if (key in first_dict) and (key in second_dict):
                array_of_values = []

                first_value = first_dict[key]
                second_value = second_dict[key]

                if isinstance(first_value, list):
                    array_of_values.extend(first_value)
                else:
                    array_of_values.append(first_value)

                if isinstance(second_value, list):
                    array_of_values.extend(second_value)
                else:
                    array_of_values.append(second_value)

                joint_dictionary[key] = array_of_values

        return joint_dictionary

    @staticmethod
    def normalize(dictionary):
        normalized_dictionary = copy.deepcopy(dictionary)

        for key, value in normalized_dictionary.items():
            minimal_value = min(value)
            maximum_value = max(value)

            difference = maximum_value - minimal_value

            for i in range(len(value)):
                value[i] = (value[i] - minimal_value) / difference

        return normalized_dictionary

    @staticmethod
    def get_characteristic_of_dictionary(dictionary):
        characteristic_dictionary = {}

        data_frame = pd.DataFrame(dictionary)
        dispersion = data_frame.var()

        for key, value in dictionary.items():
            series = pd.Series(value)

            characteristic_dictionary[f'Мин. ({key})'] = [min(value)]
            characteristic_dictionary[f'Макс. ({key})'] = [max(value)]
            characteristic_dictionary[f'Мода {key}'] = [float(series.mode()[0])]
            characteristic_dictionary[f'Медиана ({key})'] = [series.median()]
            characteristic_dictionary[f'Ср. арифметическое ({key})'] = [series.mean()]
            characteristic_dictionary[f'Ср. отклонение ({key})'] = [series.std()]
            characteristic_dictionary[f'Ср. геометрическое ({key})'] = [np.exp(np.log(value).mean())]
            characteristic_dictionary[f'Дисперсия ({key})'] = [dispersion[key]]

        return characteristic_dictionary
