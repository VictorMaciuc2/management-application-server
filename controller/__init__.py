from flask import Flask
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_object('database.database_config.Config')
db=SQLAlchemy(app)




@app.route('/')
def index():
    return "Hello, World!"

@app.route('/people')
def getNames():
    return {
        'people': ['Filip']
    }

if __name__ == '__main__':
    app.run()

