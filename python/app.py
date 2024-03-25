from flask import Flask, render_template
from os import path
import pandas as pd

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug = True)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')