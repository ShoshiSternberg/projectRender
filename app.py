from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/do')
def do_some_logic():
    x = int(request.args.get('x', ''))
    return f'{x*x}'
