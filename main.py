from subprocess import run, PIPE
import traceback
from random import randint, choice

from flask import logging, Flask, render_template, request, session

import db

app = Flask(__name__)
app.secret_key = 'eTa0xsOaErsi1rRX0ikFlMbjEakNuykZ'


@app.route('/')
def index():
    not_done = db.read_not_done_text_from_table()
    text_id, text, _ = choice(not_done)
    session['text_id'] = text_id
    session['text'] = text
    return render_template('index.html', text=text)


@app.route('/audio', methods=['POST'])
def audio():
    text_id = session.pop('text_id', None)
    text = session.pop('text', None)
    text = text.strip()
    audio_filename = text.replace(" ", '_') + '.wav'
    try:
        with open(audio_filename, 'wb') as f:
            f.write(request.data)
        db.update_table_for_done_text(text_id, audio_filename)
        return "file has been saved"
    except Exception as e:
        print(traceback.format_exc())
        return "Not saved"


if __name__ == "__main__":
    app.logger = logging.getLogger('audio-gui')
    app.run(threaded=True)
