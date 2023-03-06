import json

from flask import Flask, render_template, request
import jinja2
import pandas as pd

from Experiment.ExperimentEnum import ExperimentEnum
from Experiment.ExperimentsPolygon import ExperimentsPolygon
from Storage.SqliteDataStorage import SqliteDataStorage
from Utils.Utils import Utils

app = Flask(__name__,
            static_folder='web/static',
            template_folder='web/templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_modes')
def get_modes():
    return json.dumps(ExperimentEnum.get_modes())


@app.route('/process_form')
def process_form():
    try:
        form_data = json.loads(request.args['data'])

        modes = list(map(lambda mode: ExperimentEnum.from_string(mode), form_data['selected_modes']))
        keys_lengths = form_data['keys_lengths']
        max_message_length = form_data['max_message_length']
        amount_of_experiments = form_data['amount_of_experiments']
        duration_multiplier = form_data['duration_multiplier']

        if amount_of_experiments > 1000:
            raise Exception('Системное ограничение в количество испытаний (<= 1.000)')

        if max_message_length > 100000:
            raise Exception('Системное ограничение в максимальную длину строки (<100.000)')

        experiment_polygon = ExperimentsPolygon(modes, amount_of_experiments, keys_lengths,
                                                max_message_length, duration_multiplier)

        experiments_result = experiment_polygon.process()

        result_data = {
            'status': True,
            'data': experiments_result,
            'normalized': Utils.normalize(experiments_result),
            'characteristic': Utils.get_characteristic_of_dictionary(experiments_result),
            'correlation': pd.DataFrame(experiments_result).corr().to_dict()
        }

        print(f'Added new: {SqliteDataStorage.instance().add_data(result_data)}')

        return json.dumps(result_data)

    except(Exception, ) as e:
        return json.dumps({
            'status': False,
            'error': str(e)
        })


if __name__ == "__main__":
    app.run()
