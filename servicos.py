from __init__ import app
import os
from flask import request, render_template
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
        

if __name__=='main':
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port = port)