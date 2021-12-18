from flask import Flask, jsonify, request
from config import *


app = Flask(__name__)

VK_DATA = {'Ivan': 'id797'}

@app.route(f"/vk_id/<username>", methods=['GET'])
def get_id(username):
    if username in VK_DATA:
        return jsonify({"vk_id": str(VK_DATA[username])}), 200
    else:
        return jsonify({}), 404

@app.route(f"/vk_id/utils/create/<username>", methods=['POST'])
def create(username):
    id = request.get_json()['id']
    VK_DATA[username] = str(id)
    return jsonify('OK'), 201

@app.route(f"/vk_id/utils/delete/<username>", methods=['DELETE'])
def delete(username):
    if username in VK_DATA:
        del VK_DATA[username]
        return jsonify('OK'), 204
    else:
         return jsonify('User does not exist'), 404 

if __name__ == "__main__":
    app.run(host=MOCK_HOST, port=MOCK_PORT)
