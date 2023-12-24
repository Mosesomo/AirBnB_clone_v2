#!/usr/bin/python3
"""script that starts a Flask web application:
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page: (inside the tag BODY
    """

    states_val = storage.all(State).values()
    sorted_states = sorted(states_val, key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """method to handle @app.teardown_appcontext
    """

    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
