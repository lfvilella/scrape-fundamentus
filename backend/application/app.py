import flask

import debugger
import tasks


debugger.initialize_flask_server_debugger_if_needed()

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def running():
    return flask.jsonify({'detail': 'Running...'}), 200


@app.route('/scraper/', methods=['POST'])
def run_scraper():
    """Run Scraper

    Expected JSON body: {'assets': ['TICKET1', 'TICKET2']}
    """

    if not flask.request.json:
        flask.abort(400)

    data = flask.request.json.get('assets')
    if not data or not isinstance(data, list):
        flask.abort(400)

    result = tasks.get_assets_results(data)

    return flask.jsonify({'results': result}), 200
