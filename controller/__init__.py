from flask import Flask
from flask_cors import CORS, cross_origin
from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user
from flask_sqlalchemy import SQLAlchemy
from domain import User

from main.main import app
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()


