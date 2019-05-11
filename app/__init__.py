from flask import Flask, jsonify

app = Flask(__name__)

app.route('/')
def index():
    return jsonify({ 'message': 'The Webapp Is Running!' })

if __name__ == "__main__":
    app.run('0.0.0.0', port=5050)
