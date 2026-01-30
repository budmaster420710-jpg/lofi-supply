from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        beats = [f for f in os.listdir('static/beats') if f.endswith(('.mp3', '.wav'))]
    except FileNotFoundError:
        beats = []
    return render_template('index.html', beats=beats)

@app.route('/license')
def license_page():
    return render_template('license.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

