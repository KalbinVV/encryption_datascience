import pandas as pd

from Experiment.ExperimentEnum import ExperimentEnum
from Experiment.ExperimentsPolygon import ExperimentsPolygon

experiments_polygon = ExperimentsPolygon(
    [
        ExperimentEnum.Blowfish
    ],
    amount_of_experiments=1,
    max_power_of_two=10,
    max_length_of_message=1000,
    duration_multiplier=1000
)

df = pd.DataFrame(experiments_polygon.process())
print(df)
