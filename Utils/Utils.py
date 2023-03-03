class Utils:
    @staticmethod
    def union_dicts(first_dict: dict, second_dict: dict):
        if len(first_dict) == 0:
            return second_dict
        elif len(second_dict) == 0:
            return first_dict

        joint_dictionary = first_dict | second_dict

        for key in joint_dictionary.keys():
            if key in second_dict and key in first_dict:
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
