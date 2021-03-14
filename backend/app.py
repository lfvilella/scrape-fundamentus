""" App.py

This module is the flask API that handles endpoints.
"""

import flask

from . import debugger
from . import tasks


debugger.initialize_flask_server_debugger_if_needed()

app = flask.Flask(__name__)


@app.route('/api/v.1/', methods=['GET'])
def running():
    """Running

    Note: Endpoint to check if API is running.

    Returns:
        flask.jsonify: {'detail': 'Running...'}
    """
    return flask.jsonify({'detail': 'Running...'}), 200


@app.route('/api/v.1/scraper/', methods=['POST'])
def run_scraper():
    """Run Scraper

    Expected JSON body: {'assets': ['TICKET1', 'TICKET2']}

    Returns Example:
        flask.jsonify:
          {
            'results': [
                {
                    'ticket': 'ABCD1',
                    'subsector': 'SUBSECTOR',
                    'div_yield': '1,1%',
                    'p_l': '11,11',
                    'p_vp': '1,1',
                    'ebitda': '11,11,
                    'roe': '11%',
                    'roic': '1,0%',
                    'min_price': '0,00',
                    'max_price': '0,00',
                    'price': '0,00',
                }
            ]
          }
    """
    if not flask.request.json:
        flask.abort(400)

    data = flask.request.json.get('assets')
    if not data or not isinstance(data, list):
        flask.abort(400)

    results, errors = tasks.get_assets_results(data)

    return flask.jsonify({'results': results, 'errors': errors}), 200
