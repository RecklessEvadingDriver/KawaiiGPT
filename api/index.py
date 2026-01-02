"""
Vercel serverless function for KawaiiGPT API
"""
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    """Chat API endpoint for Vercel"""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Placeholder response - integrate with actual backend
        response_text = "KawaiiGPT API is running on Vercel! UwU"
        
        return jsonify({
            'response': response_text,
            'model': 'kawaii-3-amp'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check for Vercel"""
    return jsonify({
        'status': 'healthy',
        'service': 'KawaiiGPT-Vercel',
        'version': 'K2.5-Latest:301025'
    })
