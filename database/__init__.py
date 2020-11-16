
from database.database_config import Config
from flask_sqlalchemy import SQLAlchemy

from domain.Skill import Skill
from domain.Client import Client
from domain.Technology import Technology
from domain.Department import Department
from domain.User import User
from domain.Project import Project
from domain.ReportSession import ReportSession
from domain.Report import Report
from domain.Project_Technology import Project_Technology
from domain.User_Project import User_Project,db

db.create_all()

