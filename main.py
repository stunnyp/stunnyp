from flask import Flask, jsonify, request
from model.twit import Twit

twits = []

app = Flask(__name__)

@app.route('/ping', methods = ['GET'])
def ping():
    return jsonify({'response': 'pong'})

@app.route('/twit', methods = ['POST'])
def create_twit():
    '''{'body': 'Hello world', 'author' : '@aqaguy'}'''
    twit_json = request.get_json()
    twit = Twit(twit_json['body'], twit_json['author'])
    twits.append(twit)
    return jsonify({'status':'success'})

@app.route('/twit', methods = ['GET'])
def read_twit():
    return jsonify({'twits' : twits})

if __name__ == '__main__':
    app.run(debug=True)
