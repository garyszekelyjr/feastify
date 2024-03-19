from flask import Flask, jsonify, render_template, redirect, request
from flask_login import LoginManager, login_required, logout_user, current_user
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models.base import Base
from models.user import User

app = Flask(__name__, template_folder='build', static_folder='build/assets')
authentication = LoginManager(app)
engine = create_engine('sqlite:///db.sqlite')

Base.metadata.create_all(engine)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/authenticated')
def authenticated():
    return jsonify(current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return index()
    else:
        pass


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return index()
    else:
        pass


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


with Session(engine) as session:
    @authentication.user_loader
    def load_user(id):
        return session.get(User, id)
