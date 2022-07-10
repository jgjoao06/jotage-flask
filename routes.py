from flask import request, render_template, Response
from __init__ import app
import request_link
import leads

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/link_publico', methods=['GET'])
def link_publico():
    if request.method == 'GET':
        resp = request.json 
        link_exact = request_link.retornaLink(resp['email'], resp['api_token'])
        return link_exact

@app.route('/leads_rd', methods=['POST'])
def leads_rd():
    if request.method == 'POST':
        resp = request.json[0]
        resposta = leads.preencheLista(resp)
        if resposta == "ok":
            return Response("200")


app.run(host='0.0.0.0', port=5000)