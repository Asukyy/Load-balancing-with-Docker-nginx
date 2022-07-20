from flask import request, Flask 
import json

app1=Flask(value)
@app1.route('/')

def index():
    return 'Hello, World! mais cest lapp 2'

if value == 'app1':
    app1.run(debug=True, host='0.0.0.0')