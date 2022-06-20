from flask import request, render_template
from __init__ import app
import request_link

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/link_publico', methods=['GET'])
def link_publico():
    if request.method == 'GET':
        resp = request.json 
        link_exact = request_link.retornaLink(resp['email'], resp['api_token'])
        return link_exact

app.run(host='0.0.0.0', port=5000)