#!/usr/bin/python3
"""starts a Flask web application:
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """display a HTML page
    """

    states = storage.all(State).values()
    if id is not None:
        id = "{}.{}".format(State, id)
    return render_template('9-states.html', states=states, state_id=id)


@app.teardown_appcontext
def teardown_db(exception):
    """Declare a method to handle @app.teardown_appcontext
    """

    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
