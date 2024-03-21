from flask import Flask, request
import json
from helpers import *
from monaa import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/monaa/', methods=['POST'])
def monaa():
    data = request.json
    if not data:
        return jsonify({'error': 'No data received'}), 400

    if not "lines" in data:
        return jsonify({'error': 'Missing lines in request'}), 400

    if not "regex" in data:
        return jsonify({'error': 'Missing regex in request'}), 400
        
    file = data['lines']
    regex = data['regex']

    result = monaa_handler(file, regex)
    
    return json_response("monaa search success", regex=regex, monaa_result={"lines": result})