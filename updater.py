from flask import Flask, json, request, render_template, \
                  g, jsonify
from flask import Response
import os

JSON_DATA = 'r270/update/update.json'

app = Flask(__name__)
app.config.from_object(__name__)

def import_data():
    f = open(app.config['JSON_DATA'], 'r')
    data = json.load(f)
    f.close()
    return data

@app.before_request
def before_request():
    g.data = import_data()

@app.route('/r270/update', methods = ['POST',  'GET'])
def api_message():

    print "headers: %s\n" % (request.headers['Content-Type'])
#    fp = open(app.config['JSON_DATA'], 'r')
    fp = open('r270/update/update.json', "r")
#    content = fp.read()
    print fp.read()
    fp.seek(0)

#    dat = json.loads(content) # your JSON serialized data
    data = json.load(fp)
    dat = json.dumps(data)

#    jsonResponse = json.dumps(content)
#    jsonResponse = json.dumps({'file_content':content})     
#    resp = Response(jsonResponse, status=200, mimetype="application/json")
    resp = Response(response=dat, status=200, mimetype="application/json")
    fp.close()
    return(resp)
'''
    list = [
        {'param': 'foo', 'val': 2},
        {'param': 'bar', 'val': 10}
    ]
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    return jsonify(results=list)
'''
"""
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"
"""

@app.route('/')
def hello_world():
        return 'Hello World!\n'

if __name__ == '__main__':
        app.debug = True
        app.port = 5000
        app.run(debug=True)

