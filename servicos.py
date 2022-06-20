from __init__ import app
import os
from flask import request, render_template

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

if __name__=='main':
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port = port)
