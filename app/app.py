import os
from flask import Flask, jsonify

app = Flask(__name__)

# HIGH-ENTROPY FAKE SECRET TO TRIGGER GITLEAKS DETECTION
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
GENERIC_PRIVATE_TOKEN = "xoxb-123456789012-1234567890123-456789012345678901234567"

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
