from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head><title>Marrakech Guide</title></head>
    <body>
        <h1>Marrakech Travel Guide</h1>
        <p>Simple test page - deployment works!</p>
        <p>Once this works, we'll add the full guide.</p>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)