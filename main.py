import pandas as pd

from Experiment.ExperimentEnum import ExperimentEnum
from Experiment.ExperimentsPolygon import ExperimentsPolygon

experiments_polygon = ExperimentsPolygon(
    [
        # ExperimentEnum.AES_ECB,
        # ExperimentEnum.AES_CBC,
        ExperimentEnum.AES_CFB,
        ExperimentEnum.AES_OFB,
        ExperimentEnum.AES_CTR,
        ExperimentEnum.AES_OpenPGB,
        ExperimentEnum.AES_CCM,
        ExperimentEnum.AES_EAX,
        # ExperimentEnum.AES_SIV,
        ExperimentEnum.AES_GCM,
        ExperimentEnum.AES_OCB
    ],
    keys_length_array=[16, 24, 32],
    amount_of_experiments=100,
    max_length_of_message=1000,
    duration_multiplier=1000
)

df = pd.DataFrame(experiments_polygon.process())
df.to_excel('./result.xlsx')
