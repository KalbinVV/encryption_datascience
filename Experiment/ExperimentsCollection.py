from Utils.Utils import Utils


class ExperimentsCollection:
    def __init__(self, experiments: list, amount_of_experiments: int):
        self.__experiments = experiments
        self.__amount_of_experiments = amount_of_experiments

    def process(self):
        result = dict()

        for _ in range(self.__amount_of_experiments):
            for experiment in self.__experiments:
                result = Utils.union_dicts(result, experiment.process())

        return result
