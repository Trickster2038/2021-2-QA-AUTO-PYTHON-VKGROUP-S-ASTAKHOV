#!/usr/bin/env python3.8

import os
import random
import threading
from flask import Flask, jsonify, request

import settings

app = Flask(__name__)

KLK = {'g': 5}
SURNAME_DATA = {}


@app.route('/get_surname/<name>', methods=['GET'])
def get_user_surname(name):
    if surname := SURNAME_DATA.get(name):
        return jsonify(surname), 200
    else:
        return jsonify(f'Surname for user "{name}" not found'), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    KLK['g'] += 1
    print(KLK)
    KLK['p'] = "gg"
    name = request.get_json()['name']
    if name in SURNAME_DATA:
        return jsonify(f'User {name} already exist'), 404
    else:
        SURNAME_DATA['name'] = "gg"
        return jsonify(f'User {name} created'), 200

def shutdown_stub():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_stub()
    return jsonify(f'Ok, exiting'), 200


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT,
    })

    server.start()
    return server