# file: HealthWatch/app.py

import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from mock_fitbit_data import mock_data
from models import db, User

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db.init_app(app)
migrate = Migrate(app, db)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        profile_picture = 'static/images/profile_mockup.jpg'  # Default profile picture for now
        bio = request.form.get('bio', '')  # Optional bio

        try:
            # Check if the username or email is already taken
            if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
                flash('Username or email already taken!')
                return redirect(url_for('register'))
            
            # Create a new user
            new_user = User(username=username, email=email, profile_picture=profile_picture, bio=bio)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('User successfully registered!')
            return redirect(url_for('login'))
        
        except Exception as e:
            print(f"Error during registration: {e}")
            flash('An error occurred during registration. Please try again.')
            return redirect(url_for('register'))
    
    return render_template('register.html')

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

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
            return redirect(url_for('dashboard'))
        flash('Invalid username or password!')
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        flash('You are not logged in. Please log in to continue.')
        return redirect(url_for('login'))
    
    user = User.query.filter_by(username=session['username']).first()
    
    if request.method == 'POST':
        user.email = request.form['email']
        user.bio = request.form['bio']
        if 'password' in request.form and request.form['password']:
            user.set_password(request.form['password'])
        
        if 'profile_picture' in request.files:
            file = request.files['profile_picture']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                user.profile_picture = file_path
        
        db.session.commit()
        flash('Profile updated successfully!')
        return redirect(url_for('dashboard'))
    
    return render_template('dashboard.html', user=user)

@app.route('/health_recommendations')
def health_recommendations():
    if 'username' not in session:
        return redirect(url_for('login'))
    recommendations = mock_data.get('health_recommendations', [])
    return render_template('health_recommendations.html', recommendations=recommendations)

@app.route('/historical_data')
def historical_data():
    if 'username' not in session:
        return redirect(url_for('login'))
    data = mock_data.get('historical_data', [])
    return render_template('historical_data.html', historical_data=data)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
