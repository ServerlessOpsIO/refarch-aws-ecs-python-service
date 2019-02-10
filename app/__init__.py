#!env python3

'''Example Flask app for ECS'''
from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    '''Hello World'''
    message = {'message': 'Hello, World!'}
    resp = jsonify(message)
    resp.status_code = 200

    return resp


@app.route('/health', methods=['GET'])
def health():
    '''Health endpoint'''
    message = {'health': 'OK'}
    resp = jsonify(message)
    resp.status_code = 200

    return resp


