from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/test')
def test():
    return jsonify({'message': 'This is test route'})
