from enum import Enum

from Experiment.AESExperiment import AESExperiment
from Experiment.BlowfishExperiment import BlowfishExperiment
from Experiment.ChaCha20Experiment import ChaCha20Experiment
from Experiment.Rc4Experiment import Rc4Experiment
from Experiment.Salsa20Experiment import Salsa20Experiment


class ExperimentEnum(Enum):
    AES = 0
    Blowfish = 1
    ChaCha20 = 2
    Rc4 = 3
    Salsa20 = 5

    @classmethod
    def from_enum(cls, value):
        if value == cls.AES:
            return AESExperiment
        elif value == cls.Blowfish:
            return BlowfishExperiment
        elif value == cls.ChaCha20:
            return ChaCha20Experiment
        elif value == cls.Rc4:
            return Rc4Experiment
        elif value == cls.Salsa20:
            return Salsa20Experiment
