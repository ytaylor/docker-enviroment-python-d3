from iteration_utilities import flatten
from flask import Flask, jsonify
from pathlib import Path
import pandas as pd
import json


data_path = Path(__file__).resolve().parent.parent / 'data'
static_path = Path(__file__).resolve().parent / 'static' / 'dist'
#print('data path: ' + str(data_path))
#print('static path: ' + str(static_path))

app = Flask(__name__, static_folder=static_path)

@app.route("/")
def index():
	return app.send_static_file('index.html')

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
