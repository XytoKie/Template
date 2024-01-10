import hashlib
import json
from time import time

import flask
from flask import Flask, jsonify, request
from uuid import uuid4

# create /healthcheck endpoint
@app.route('/healthcheck', methods=['GET', 'POST'])
def health_check():
    response = {
       'health': 'OK'
    }
    return jsonify(response), 200


# start server on port 6392
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6392)
