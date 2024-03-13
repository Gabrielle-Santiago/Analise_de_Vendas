from flask import Flask, render_template
from os import path
import pandas as pd

app = Flask(__name__)

df = app.template_folder = path.abspath('html/index.html')

def index():
    return render_template('index.html', table = df.to.html(index = False))

if __name__ == '__main__':
    app.run(debug = True)