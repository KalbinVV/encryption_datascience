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
    def from_string(cls, value):
        return {
            'Blowfish': cls.Blowfish,
            'ChaCha20': cls.ChaCha20,
            'Rc4': cls.Rc4,
            'Salsa20': cls.Salsa20,
            'AES_ECB': cls.AES_ECB,
            'AES_CBC': cls.AES_CBC,
            'AES_CFB': cls.AES_CFB,
            'AES_OFB': cls.AES_OFB,
            'AES_CTR': cls.AES_CTR,
            'AES_OpenPGB': cls.AES_OpenPGB,
            'AES_CCM': cls.AES_CCM,
            'AES_EAX': cls.AES_EAX,
            'AES_SIV': cls.AES_SIV,
            'AES_GCM': cls.AES_GCM,
            'AES_OCB': cls.AES_OCB
        }[value]

    @classmethod
    def from_enum(cls, value):
        return {
            cls.Blowfish: BlowfishExperiment,
            cls.ChaCha20: ChaCha20Experiment,
            cls.Rc4: Rc4Experiment,
            cls.Salsa20: Salsa20Experiment,
            cls.AES_ECB: AESECBExperiment,
            cls.AES_CBC: AESCBCExperiment,
            cls.AES_CFB: AESCFBExperiment,
            cls.AES_OFB: AESOFBExperiment,
            cls.AES_CTR: AESCTRExperiment,
            cls.AES_OpenPGB: AESOpenPGBExperiment,
            cls.AES_CCM: AESCCMExperiment,
            cls.AES_EAX: AESEAXExperiment,
            cls.AES_SIV: AESSIVExperiment,
            cls.AES_GCM: AESGCMExperiment,
            cls.AES_OCB: AESOCBExperiment
        }[value]

    @classmethod
    def get_modes(cls):
        return [
            {'name': 'Blowfish', 'status': 'Main'},
            {'name': 'ChaCha20', 'status': 'Dev'},
            {'name': 'Salsa20', 'status': 'Dev'},
            {'name': 'Rc4', 'status': 'Main'},
            {'name': 'AES_ECB', 'status': 'Dev'},
            {'name': 'AES_CBC', 'status': 'Dev'},
            {'name': 'AES_CFB', 'status': 'Main'},
            {'name': 'AES_OFB', 'status': 'Main'},
            {'name': 'AES_CTR', 'status': 'Main'},
            {'name': 'AES_OpenPGB', 'status': 'Main'},
            {'name': 'AES_CCM', 'status': 'Main'},
            {'name': 'AES_EAX', 'status': 'Main'},
            {'name': 'AES_SIV', 'status': 'Dev'},
            {'name': 'AES_GCM', 'status': 'Main'},
            {'name': 'AES_OCB', 'status': 'Main'}
        ]
