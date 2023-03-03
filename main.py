import pandas as pd

from Experiment.ExperimentEnum import ExperimentEnum
from Experiment.ExperimentsPolygon import ExperimentsPolygon

experiments_polygon = ExperimentsPolygon(
    [
        ExperimentEnum.Rc4,
        ExperimentEnum.Salsa20,
        ExperimentEnum.Blowfish,
        ExperimentEnum.AES
    ],
    keys_length_array=[32],
    amount_of_experiments=100,
    max_length_of_message=1000,
    duration_multiplier=1000
)

df = pd.DataFrame(experiments_polygon.process())
print(df)