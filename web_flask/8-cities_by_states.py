#!/usr/bin/python3
"""script that starts a flask web server"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display a HTML page
    """

    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda s: s.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """method to handle @app.teardown_appcontext
    """

    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
