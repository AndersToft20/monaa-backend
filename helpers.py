from flask import jsonify

def error_response(msg, **kwargs):
    return jsonify({'status': 'ERROR', 'message': msg, **kwargs}), 400

def json_response(msg, **kwargs):
    return jsonify({'status': 'success', 'message': msg, **kwargs}), 200

