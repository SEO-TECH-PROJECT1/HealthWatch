# File: HealthWatch/app.py

# File: HealthWatch/app.py

import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from mock_fitbit_data import fetch_fitbit_data
from datetime import datetime

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    profile_picture = db.Column(db.String(250), nullable=True)
    joined_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    bio = db.Column(db.Text, nullable=True)
    password_hash = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_next_profile_pic_number():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    numbers = [int(f.split('_')[-1].split('.')[0]) for f in files if f.startswith('new_profile_pic')]
    return max(numbers, default=0) + 1

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        profile_picture = 'static/images/profile_mockup.jpg'
        bio = request.form.get('bio', '')

        try:
            if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
                flash('Username or email already taken!')
                return redirect(url_for('register'))
            
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
    
    # Fetch the latest activity data
    daily_steps = fetch_fitbit_data('daily_steps')
    heart_rate = fetch_fitbit_data('heart_rate')
    sleep_pattern = fetch_fitbit_data('sleep_pattern')

    # Get the most recent data
    latest_steps = daily_steps[-1] if daily_steps else None
    
    # Format the data for display
    latest_activity = {
        'steps': f"{latest_steps['steps']} steps on {latest_steps['date']}" if latest_steps else "No data available",
        'heart_rate': f"Average heart rate of {heart_rate['value']} bpm on {heart_rate['date']}" if heart_rate else "No data available",
        'sleep_pattern': f"{sleep_pattern['duration']} minutes of sleep with {sleep_pattern['efficiency']}% efficiency on {sleep_pattern['date']}" if sleep_pattern else "No data available"
    }

    try:
        activity_labels = [data['date'] for data in daily_steps[-30:]]  # Last 7 days
        activity_data = [data['steps'] for data in daily_steps[-30:]]  # Last 7 days
    except (KeyError, TypeError):
        flash('Error retrieving activity data')
        activity_labels = []
        activity_data = []

    if request.method == 'POST':
        user.email = request.form['email']
        user.bio = request.form['bio']
        if 'password' in request.form and request.form['password']:
            user.set_password(request.form['password'])
        
        if 'profile_picture' in request.files:
            file = request.files['profile_picture']
            if file and allowed_file(file.filename):
                number = get_next_profile_pic_number()
                filename = f'new_profile_pic_{number}.jpg'
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                user.profile_picture = f'uploads/{filename}'
        
        db.session.commit()
        flash('Profile updated successfully!')
        return redirect(url_for('dashboard'))
    
    return render_template('dashboard.html', user=user, latest_activity=latest_activity, activity_labels=activity_labels, activity_data=activity_data)

@app.route('/health_recommendations')
def health_recommendations():
    if 'username' not in session:
        return redirect(url_for('login'))
    user = User.query.filter_by(username=session['username']).first()
    recommendations = fetch_fitbit_data('health_recommendations')
    historical_data = fetch_fitbit_data('historical_data')
    return render_template('health_recommendations.html', user=user, recommendations=recommendations, historical_data=historical_data)

@app.route('/historical_data')
def historical_data():
    if 'username' not in session:
        return redirect(url_for('login'))
    data = fetch_fitbit_data('historical_data')
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