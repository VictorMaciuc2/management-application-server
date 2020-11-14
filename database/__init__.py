
from database.database_config import Config
from flask_sqlalchemy import SQLAlchemy

from domain.Skill import Skill
from domain.Client import Client
from domain.Technology import Technology
from domain.Department import Department
from domain.User import User
from domain.Project import Project
from domain.ReportSession import ReportSession,db
db.create_all()
#app.config.from_object(Config)
#app.config['DEBUG']=True
