import json

from flask import Flask, render_template, request
import jinja2

from Experiment.ExperimentEnum import ExperimentEnum
from Experiment.ExperimentsPolygon import ExperimentsPolygon
from Utils.Utils import Utils

app = Flask(__name__,
            static_folder='web/static',
            template_folder='web/templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_form')
def process_form():
    form_data = json.loads(request.args['data'])

    modes = list(map(lambda mode: ExperimentEnum.from_string(mode), form_data['selected_modes']))
    keys_lengths = form_data['keys_lengths']
    max_message_length = form_data['max_message_length']
    amount_of_experiments = form_data['amount_of_experiments']
    duration_multiplier = form_data['duration_multiplier']

    experiment_polygon = ExperimentsPolygon(modes, amount_of_experiments, keys_lengths,
                                            max_message_length, duration_multiplier)

    experiments_result = experiment_polygon.process()

    result_data = {
        'data': experiments_result,
        'normalized': Utils.normalize(experiments_result),
        'characteristic': Utils.get_characteristic_of_dictionary(experiments_result)
    }

    return json.dumps(result_data)


if __name__ == "__main__":
    app.run()
