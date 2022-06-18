from flask import request, render_template
from __init__ import app
import funcoes

@app.route('/webhook/link_publico', methods=['GET'])
def link_publico():
    if request.method == 'GET':
        print("Data received from Webhook is: ", request.json)
        resp = request.json
        email = resp['email'] 
        link_publico = funcoes.retornaLink(email)
        return link_publico

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

        

app.run(host='0.0.0.0', port=5000)