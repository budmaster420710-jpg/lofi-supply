import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
DIR = os.path.join(os.path.expanduser('~'), 'uploads')

@app.route('/')
def index():
    if not os.path.exists(DIR): 
        os.makedirs(DIR)
    files = sorted([f for f in os.listdir(DIR) if f.endswith('.wav')])
    return render_template('index.html', files=files)

@app.route('/stream/<path:name>')
def download_file(name):
    return send_from_directory(DIR, name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

