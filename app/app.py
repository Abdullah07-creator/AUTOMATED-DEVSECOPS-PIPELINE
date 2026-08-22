import os
from flask import Flask, jsonify

app = Flask(__name__)

# INTENTIONAL HARDCODED SECRET FOR PHASE 7 TESTING
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE_SECRET_KEY_FOR_TESTING"

@app.route('/')
def home():
    return jsonify({"status": "success", "message": "DevSecOps Pipeline App Active"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() in ['true', '1']
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
