from flask import Flask, request
import json
from helpers import *
from monaa import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/monaa/', methods=['POST'])
def monaa():
    if not "file" in request.post:
        return error_response("Missing file in request")
    if not "regex" in request.post:
        return error_response("Missing regex in request")

    file = request.post['file']
    regex = request.post.get('regex', None)

    result = monaa_handler(file, regex)
    
    return json_response("monaa search success", regex=regex, monaa_result={"lines": result})