from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from fitbit_api import FitbitAPI
import hashlib
import base64
import os
import time
import random
import string
import requests
from flask import Flask, request, redirect
from pprint import pprint
from flask_login import login_required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
CLIENT_ID = "23PFP8"
CLIENT_SECRET = "c6964127ec034058e8ccc4b33cf0cad9"
# FAPI = FitbitAPI(os.environ['CLIENT_ID'], os.environ['CLIENT_SECRET'])
FAPI = FitbitAPI(CLIENT_ID, CLIENT_SECRET)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@app.route('/')
def index():
    del session['username']
    del session['code_verifier']
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))



@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Username already taken!')
            return redirect(url_for('register'))
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('User successfully registered!')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['username'] = username
            code_verifier, code_challenge = FAPI.PCKE_generator()
            session['code_verifier'] = code_verifier
            state = FAPI.generate_random_value(32)
              # Store code_verifier in session
            return redirect(FAPI.authorize(code_challenge, state))
        flash('Invalid username or password!')
    
    return render_template('login.html')




@app.route('/dashboard')
def dashboard():
    
    if 'username' not in session:
        return redirect(url_for('login'))
    
    auth_token = request.args.get('code')
    if auth_token:
        print("AUTH_TOKEN is: ", auth_token)
    if auth_token:
        code_verifier = session.get('code_verifier')  # Retrieve code_verifier from session
        tokens = FAPI.get_tokens(auth_token, code_verifier)
        pprint(tokens)
        try:
            access_token = tokens['access_token']
        except KeyError:
            return redirect(url_for('login'))
        session['access_token'] = access_token
    return render_template('dashboard.html')


@app.route('/health')
def health():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('health.html')

@app.route('/history')
def history():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('history.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)



