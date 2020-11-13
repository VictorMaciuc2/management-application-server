from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from database import init_db
db=init_db(app)
@app.route('/')
def index():
    return "Hello, World!"

@app.route('/people')
def getNames():
    return {
        'people': ['Filip']
    }




if __name__ == '__main__':
    #db = init_db(app)
    app.run(debug=True)

