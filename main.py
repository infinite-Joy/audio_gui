from subprocess import run, PIPE
import traceback
from random import randint

from flask import logging, Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'eTa0xsOaErsi1rRX0ikFlMbjEakNuykZ'


@app.route('/')
def index():
    text = "this is done using session {}".format(randint(10, 1000))
    session['text'] = text
    return render_template('index.html', text=text)


@app.route('/audio', methods=['POST'])
def audio():
    text = session.pop('text', None)
    try:
        with open('audio.wav', 'wb') as f:
            f.write(request.data)
        return "file has been saved"
    except Exception as e:
        print(traceback.format_exc())
        return "Not saved"


if __name__ == "__main__":
    app.logger = logging.getLogger('audio-gui')
    app.run(threaded=True)
