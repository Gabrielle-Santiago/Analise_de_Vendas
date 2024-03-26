from flask import Flask, render_template
from os import path
import pandas as pd

app = Flask(__name__)

template_dir = path.abspath('../templates/')
app.template_folder = template_dir

@app.route('/')
def test():
    nome = ('Guilherme')
    return render_template('test.html', nome=nome)

if __name__ == '__main__':
    app.run(debug = True)