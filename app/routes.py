from flask import request, render_template
from __init__ import app

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

app.run(host='0.0.0.0', port=5000)