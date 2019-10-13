from flask import (Flask, render_template, redirect,
                   url_for, request, make_response,
                   flash)
import json
from options import DEFAULTS

app = Flask(__name__)
app.secret_key = 'esadfadfgadr%3w35aadfgadg!Sf'

def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:  #  if cookies gives us back something we can't turn into json
        data = {}
    return data


@app.route('/save', methods=['POST'])
def save():
    # import pdb; pdb.set_trace()
    flash('Alright, that looks awesome!')
    response = make_response(redirect(url_for('builder')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character', json.dumps(data))
    return response


@app.route('/')
def index():
    return render_template('index.html', data=get_saved_data())


@app.route('/builder')
def builder():
    return render_template(
        'builder.html',
        data = get_saved_data(),
        options = DEFAULTS
    )


app.run(debug=True)