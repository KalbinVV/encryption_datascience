import json

from Experiment.AESExperiment import AESExperiment
from Experiment.ExperimentsCollection import ExperimentsCollection
from Experiment.Rc4Experiment import Rc4Experiment
from Experiment.Salsa20Experiment import Salsa20Experiment

key = b'Hello, worlderf!'
message = b'Hello, message!'

experiments_collection = ExperimentsCollection(
    experiments=[
        Rc4Experiment(key, message, duration_multiplier=1000),
        Salsa20Experiment(key, message, duration_multiplier=1000),
        AESExperiment(key, message, duration_multiplier=1000)
    ],
    amount_of_experiments=5
)

print(json.dumps(experiments_collection.process(), indent=4))
