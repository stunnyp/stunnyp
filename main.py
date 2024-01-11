from flask import Flask, jsonify, request
from model.twit import Twit
import json

twits = []

app = Flask(__name__)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Twit):
            return {'id': obj.id, 'body': obj.body, 'author': obj.author}
        else:
            return super().default(obj)

app.json_encoder = CustomJSONEncoder
    

@app.route('/ping', methods = ['GET'])
def ping():
    return jsonify({'response': 'pong'})

@app.route('/twit', methods = ['POST'])
def create_twit():
    '''{"id": "1" , "body": "Hello world", "author" : "@aqaguy"}'''
    twit_json = request.get_json()
    twit = Twit(twit_json['id'],twit_json['body'], twit_json['author'])
    twits.append(twit.JSON())
    return jsonify({'status':'success'})

@app.route('/twit/<int:id>', methods=['PUT'])
def update_twit(id):
    update_data = request.get_json()
    for twit in twits:
        if twit['id'] == str(id):
            twit['body'] = update_data.get('body', twit['body'])
            twit['author'] = update_data.get('author', twit['author'])
            return jsonify({'status': 'success'})
    return jsonify({'status': 'error', 'message': 'Twit not found'})

@app.route('/twit/<int:id>', methods = ['DELETE'])
def delete_twit(id):
    for twit in twits:
        if twit['id'] == str(id):
            twits.remove(twit)
            return jsonify({'status': 'success'})
    return jsonify({'status': 'error', 'message': 'Twit not found'})


@app.route('/twit', methods = ['GET'])
def read_twits():
    return json.dumps({'twits' : twits})

if __name__ == '__main__':
    app.run(debug=True)
