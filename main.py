import flask
from flask import request, jsonify
import json
from pool import PoolHandler

from services.constant import STRATEGY


# Create application instance
app = flask.Flask(__name__)


def is_pool_exists(pool_id):
    pool_id = pool_id.strip()
    for pool in POOL_LIST:
        if pool_id == pool['id']:
            return True
    return False

# Create URl
@app.route('/api/v1/pool', methods=['POST'])
def post_pool():
    try:
        if (len(request.data) == 0):
            return 'Not exists parameters', 400
        parsed_pool = json.loads(request.data)
        res = PoolHandler.upsert(parsed_pool)
        if res not in ['Appended', 'Inserted']:
            return res, 400
    except AssertionError as e:
        return e, 500
    else:
        return res


@app.route('/api/v1/pool_indexes', methods=['POST'])
def get_aspect_pool():
    try:
        if (len(request.data) == 0):
            return 'Not exists parameters', 400
        parsed_data = json.loads(request.data)
        result = PoolHandler.get(parsed_data, STRATEGY)
        if (not isinstance(result, dict)):
            return result, 400
    except AssertionError as e:
        return e, 500
    else:
        return jsonify(result)

    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)