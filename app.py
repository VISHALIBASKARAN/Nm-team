from flask import Flask, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    app.logger.info('Home page visited')
    return jsonify({'message': 'Hello from microservice'})

@app.route('/error')
def error():
    app.logger.error('Simulated error occurred!')
    return jsonify({'error': 'Something went wrong'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
