from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def root():
    return jsonify(message="I'm root"),  200

@app.route('/python')
def python():
    return jsonify(message="I'm Python"),  200

if __name__ == '__main__':
    port = int(os.environ.get('PORT',  5000))
    app.run(host='0.0.0.0', port=port)
