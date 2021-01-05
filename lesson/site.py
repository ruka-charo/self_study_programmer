from flask import Flask

app = Flask('Ruka')
@app.route('/')

def index():
    return 'Hello, World!'

app.run(port = 8000)
