from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/people')
def getNames():
    return {
        'people': ['Filip','Vlad']
    }

if __name__ == '__main__':
    app.run(debug=True)

a = 3