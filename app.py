"""
KawaiiGPT Web Server
Flask-based web interface for hosting on platforms like Heroku
"""
from flask import Flask, render_template, request, jsonify, session
import os
import json
import hashlib
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))

# Configuration
PORT = int(os.environ.get('PORT', 5000))
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Chat endpoint"""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Get or create session
        if 'conversation' not in session:
            session['conversation'] = []
        
        # Add user message to conversation
        session['conversation'].append({
            'role': 'user',
            'content': user_message
        })
        
        # Here you would integrate with the actual KawaiiGPT backend
        # For now, return a placeholder response
        response_text = "KawaiiGPT web interface is running! Connect your API endpoints here."
        
        session['conversation'].append({
            'role': 'assistant',
            'content': response_text
        })
        
        return jsonify({
            'response': response_text,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/clear', methods=['POST'])
def clear_conversation():
    """Clear conversation history"""
    session['conversation'] = []
    return jsonify({'status': 'success'})

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'KawaiiGPT',
        'version': 'K2.5-Latest:301025'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
