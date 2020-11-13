
def init_db(app):
    from flask_sqlalchemy import SQLAlchemy
    database_uri="sqlite:///../database.db"
    db=SQLAlchemy()
    db.init_app(app)
    from domain.Skill import Skill
    app.config['SQLALCHEMY_DATABASE_URI']=database_uri
    app.config['DEBUG']=True
    with app.app_context():
        db.create_all()# this creates tables in db, to work ALL MODELS NEED TO BE IMPORTED HERE

    return db