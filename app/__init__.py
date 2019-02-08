#!env python3

'''Example Flask app for ECS'''
from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    '''Entry point'''
    message = {'message': 'Hello, World!'}
    resp = jsonify(message)
    resp.status_code = 200

    return resp

