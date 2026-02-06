from flask import Flask, render_template
import os

app = Flask(__name__)

# Minimal data
MARRAKECH_DATA = {
    "title": "Marrakech Travel Guide",
    "subtitle": "Cool Experiences for Your Trip"
}

@app.route('/')
def index():
    return render_template('index.html', data=MARRAKECH_DATA)

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)