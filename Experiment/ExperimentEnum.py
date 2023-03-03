from enum import Enum

from Experiment.AES.AESCBCExperiment import AESCBCExperiment
from Experiment.AES.AESCCMExperiment import AESCCMExperiment
from Experiment.AES.AESCFBExperiment import AESCFBExperiment
from Experiment.AES.AESCTRExperiment import AESCTRExperiment
from Experiment.AES.AESEAXExperiment import AESEAXExperiment
from Experiment.AES.AESECBExperiment import AESECBExperiment
from Experiment.AES.AESGCMExperiment import AESGCMExperiment
from Experiment.AES.AESOCBExperiment import AESOCBExperiment
from Experiment.AES.AESOFBExperiment import AESOFBExperiment
from Experiment.AES.AESOpenPGBExperiment import AESOpenPGBExperiment
from Experiment.AES.AESSIVExperiment import AESSIVExperiment
from Experiment.Legacy.BlowfishExperiment import BlowfishExperiment
from Experiment.Legacy.ChaCha20Experiment import ChaCha20Experiment
from Experiment.Legacy.Rc4Experiment import Rc4Experiment
from Experiment.Legacy.Salsa20Experiment import Salsa20Experiment


class ExperimentEnum(Enum):
    # Legacy
    Blowfish = 0
    ChaCha20 = 1
    Rc4 = 2
    Salsa20 = 3
    # AES
    AES_ECB = 4
    AES_CBC = 5
    AES_CFB = 6
    AES_OFB = 7
    AES_CTR = 8
    AES_OpenPGB = 9
    AES_CCM = 10
    AES_EAX = 11
    AES_SIV = 12
    AES_GCM = 13
    AES_OCB = 14

    # Make it more readable, may new enum in python3.10
    @classmethod
    def from_enum(cls, value):
        if value == cls.Blowfish:
            return BlowfishExperiment
        elif value == cls.ChaCha20:
            return ChaCha20Experiment
        elif value == cls.Rc4:
            return Rc4Experiment
        elif value == cls.Salsa20:
            return Salsa20Experiment
        elif value == cls.AES_ECB:
            return AESECBExperiment
        elif value == cls.AES_CBC:
            return AESCBCExperiment
        elif value == cls.AES_CFB:
            return AESCFBExperiment
        elif value == cls.AES_OFB:
            return AESOFBExperiment
        elif value == cls.AES_CTR:
            return AESCTRExperiment
        elif value == cls.AES_OpenPGB:
            return AESOpenPGBExperiment
        elif value == cls.AES_CCM:
            return AESCCMExperiment
        elif value == cls.AES_EAX:
            return AESEAXExperiment
        elif value == cls.AES_SIV:
            return AESSIVExperiment
        elif value == cls.AES_GCM:
            return AESGCMExperiment
        elif value == cls.AES_OCB:
            return AESOCBExperiment
