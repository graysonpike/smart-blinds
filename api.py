from flask import Flask, request
import blinds
app = Flask(__name__)

@app.route('/adjust')
def hello_world():
    position = int(request.args['position'])

    # Bounds check
    if position < 0: position = 0
    if position > 100: position = 100

    blinds.adjust(position)
    