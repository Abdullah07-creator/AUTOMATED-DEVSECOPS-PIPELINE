import os
import time
from flask import Flask, jsonify

app = Flask(__name__)
START_TIME = time.time()

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "DevSecOps Production Hardened Application Active"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "uptime_seconds": round(time.time() - START_TIME, 2)
    }), 200

@app.route('/metrics')
def metrics():
    # Basic application telemetry metrics endpoint
    return jsonify({
        "app_name": "devsecops-app",
        "status": "up",
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "environment": os.environ.get('FLASK_ENV', 'production')
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() in ['true', '1']
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
