import flask
from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

@app.route('/status/ok', methods=['GET'])
def status_ok():
    return jsonify({"status": "ok", "message": "Service is running normally."}), 200

@app.route('/status/slow', methods=['GET'])
def status_slow():
    delay = random.uniform(2.0, 3.0) # sengaja dibuat lambat
    time.sleep(delay)
    return jsonify({"status": "ok", "message": f"Service is running, but responded slowly after {delay:.2f}s."}), 200

@app.route('/status/error', methods=['GET'])
def status_error():
    return jsonify({"status": "error", "message": "Internal Server Error occurred."}), 500

# Tidak perlu endpoint untuk 404, karena Flask akan menanganinya secara otomatis

if __name__ == '__main__':
    print("Simple Health Check API Server running on http://127.0.0.1:5000")
    print("Endpoints:")
    print("  - GET /status/ok")
    print("  - GET /status/slow")
    print("  - GET /status/error")
    print("  - (URL lain akan menghasilkan 404 Not Found)")
    app.run(debug=False, threaded=True, use_reloader=False)