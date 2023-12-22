#!/usr/bin/python3
"""script that starts a Flask web application
   display “n is a number” only if n is an integer
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display hello world
    """

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text="is cool"):
    """display “Python ”, followed by the value of the text
        variable
    Args:
        text (str, optional): _description_. Defaults to "is cool".

    Returns:
        _type_: _description_
    """

    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_n_is_number(n):
    """display “n is a number” only if n is an integer
    """

    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer
    """

    if isinstance(n, int):
        return render_template('5-number.html', number=n)


if __name__ == ("__main__"):
    app.run(host='0.0.0.0', port=5000)
