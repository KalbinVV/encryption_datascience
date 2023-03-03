class Utils:
    # TODO: Optimise
    @staticmethod
    def union_dicts(first_dict: dict, second_dict: dict):
        final_dict = dict()

        for key, value in first_dict.items():
            if key not in second_dict:
                final_dict[key] = value

        for key, value in second_dict.items():
            if key not in first_dict:
                final_dict[key] = value

        for key, value in first_dict.items():
            if key in second_dict:
                if not (isinstance(value, list) or isinstance(second_dict[key], list)):
                    final_dict[key] = [value, second_dict[key]]
                else:
                    if isinstance(value, list) and isinstance(second_dict[key], list):
                        final_dict[key] = [*value, *second_dict[key]]
                    elif isinstance(value, list):
                        final_dict[key] = [*value, second_dict[key]]
                    else:
                        final_dict[key] = [value, *second_dict[key]]

        return final_dict
