from flask import Flask, request
import json
from helpers import *
from monaa import *

app = Flask(__name__)


@app.route('/monaa/', methods=['POST'])
def monaa():
    if not "file" in request.files:
        return error_response("Missing file in request")
    if not "regex" in request.form:
        return error_response("Missing regex in request")

    file = request.files['file']
    if not file.filename.endswith('.txt'):
        return error_response("File format is incorrect. Only .txt files are allowed.")

    regex = request.form.get('regex', None)


    result = monaa_handler(file, regex)
    
    return json_response("monaa search success", monaa_result=result)