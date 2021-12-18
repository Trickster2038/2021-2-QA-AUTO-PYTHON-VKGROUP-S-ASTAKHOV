#!/usr/bin/env python3.8

import threading
from flask import Flask, jsonify, request
import logging
import settings
from werkzeug.serving import WSGIRequestHandler
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'file': {
        'class': 'logging.handlers.RotatingFileHandler',
        'formatter': 'default',
        'filename': 'mock_server.log',
        'maxBytes': 1024*1024,
        'backupCount': 3
    }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})

app = Flask(__name__)

SURNAME_DATA = {}

@app.route('/get_surname/<name>', methods=['GET'])
def get_user_surname(name):
    if surname := SURNAME_DATA.get(name):
        return jsonify(surname), 200
    else:
        return jsonify(f'Surname for user {name} not found'), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.get_json()['name']
    if name in SURNAME_DATA:
        return jsonify(f'User {name} already exists'), 404
    else:
        SURNAME_DATA[name] = None
        return jsonify(f'User {name} created'), 200


@app.route('/update_user/<name>', methods=['PUT'])
def update_user(name):
    surname = request.get_json()['surname']
    if name in SURNAME_DATA:
        SURNAME_DATA[name] = surname
        return jsonify(f'User {name} updated'), 200
    else:
        # SURNAME_DATA[name] = None
        return jsonify(f'User {name} does not exist'), 404


@app.route('/delete_user/<name>', methods=['DELETE'])
def delete_user(name):
    if name in SURNAME_DATA:
        del SURNAME_DATA[name]
        return jsonify(f'User {name} deleted'), 200
    else:
        return jsonify(f'User {name} does not exist'), 404


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'Ok, exiting'), 200


def run_mock():
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT,
    })

    server.start()
    return server
